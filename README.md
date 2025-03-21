# Python Project


## 脚本说明

### pandas.ipynb
- **功能**: 演示如何使用Pandas库处理表格数据。
- **内容**:
  - 创建DataFrame对象。
  - 使用不同的方式初始化DataFrame。
  - 提取DataFrame中的列和行。

### use_pdf.py
- **功能**: 解析PDF文件并将其内容转换为Markdown格式。
- **内容**:
  - 使用`pdfplumber`库提取PDF中的文本和表格。
  - 将提取的内容转换为Markdown格式。
  - 将Markdown内容保存到文件中。

### split_pdf.py
- **功能**: 将PDF文件按页分割成多个单独的PDF文件。
- **内容**:
  - 使用`PyPDF2`库读取和写入PDF文件。
  - 将输入的PDF文件按页分割并保存到指定文件夹中。

```
python split_pdf.py path/to/input.pdf --output_folder path/to/output_folder
```
```
python use_pdf.py path/to/input.pdf
```
