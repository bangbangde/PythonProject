import pandas as pd
import pdfplumber
import argparse
import os

def _sort_elements(elements):
    # 按页码->垂直位置->水平位置排序[3,7](@ref)
    sorted_elements = sorted(elements, key=lambda x: (x["page"], x["y"], x.get("x0",0)))
    
    # 处理分栏布局（以两栏为例）
    final_order = []
    current_page = -1
    column_threshold = None
    
    for elem in sorted_elements:
        if elem["page"] != current_page:
            current_page = elem["page"]
            # 计算分栏阈值（假设页面宽度为A4：595pt）
            column_threshold = 595 / 2 - 20  # 留20pt边距
            
        # 判断是否属于右栏
        if elem.get("x0", 0) > column_threshold:
            # 延迟到左栏内容之后插入
            final_order.append(("right", elem))
        else:
            final_order.append(("left", elem))
    
    # 重组分栏内容
    output = []
    left_buffer, right_buffer = [], []
    for pos, elem in final_order:
        if pos == "left":
            if right_buffer:
                output.extend(right_buffer)
                right_buffer = []
            output.append(elem)
        else:
            right_buffer.append(elem)
    output.extend(right_buffer)
    return output

def extract_elements(pdf_path):
    elements = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            # 提取表格区域坐标
            tables = page.find_tables()
            table_bboxes = [table.bbox for table in tables]
            
            # 提取文本块（过滤表格区域）
            text_blocks = []
            words = page.extract_words(x_tolerance=2, y_tolerance=3)
            current_line = []
            for word in words:
                # 判断是否在表格区域内[1,7](@ref)
                if any(word["x0"] >= bbox[0] and word["x1"] <= bbox[2] and 
                       word["top"] >= bbox[1] and word["bottom"] <= bbox[3] 
                       for bbox in table_bboxes):
                    continue
                
                # 合并成行
                if not current_line:
                    current_line.append(word)
                else:
                    last_word = current_line[-1]
                    if abs(word["top"] - last_word["top"]) < 2:
                        current_line.append(word)
                    else:
                        text_blocks.append({
                            "text": " ".join([w["text"] for w in current_line]),
                            "top": current_line[0]["top"]
                        })
                        current_line = [word]
            if current_line:
                text_blocks.append({
                    "text": " ".join([w["text"] for w in current_line]),
                    "top": current_line[0]["top"]
                })
            
            # 添加元素
            elements.extend([
                {"type": "text", "content": tb["text"], "page": page_num, "y": tb["top"]} 
                for tb in text_blocks
            ])
            
            # 添加表格
            for table in tables:
                df = pd.DataFrame(table.extract()[1:], columns=table.extract()[0])
                elements.append({
                    "type": "table", 
                    "content": df.to_markdown(index=False),
                    "page": page_num,
                    "y": table.bbox[1]
                })

            # 添加图片
            for image in page.images:
                elements.append({
                    "type": "image",
                    # 上传图片到图床，返回图片链接 f'[Image]({url})'
                    "content": f'[Image](url)',
                    "page": page_num,
                    "y": image["top"]
                })
     
    return _sort_elements(elements)

def to_md(elements):
    md = ""
    for elem in elements:
        if elem["type"] == "text":
            md += f"{elem['content']}\n\n"
        elif elem["type"] == "table":
            md += f"{elem['content']}\n\n"
    return md

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='解析PDF文件并转换为Markdown格式')
    parser.add_argument('input_pdf', type=str, help='Path to the input PDF file')

    args = parser.parse_args()
    input_pdf_path = args.input_pdf or './assets/example.pdf'
    filename = os.path.splitext(os.path.basename(input_pdf_path))[0]
    
    elements = extract_elements(input_pdf_path)
    if not os.path.exists("output"):
        os.makedirs("output")
    with open(f'output/{filename}.md', 'wb') as f:
            f.write(to_md(elements).encode())
