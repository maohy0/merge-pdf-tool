# PDF合并工具
## 📄 功能简介
这个是一个合并 pdf 的工具，可以方便的完成：
* 扫描当前目录（或指定目录）内所有 PDF 文件
* 按文件名升序合并
* 将所有页面适配为竖向 A4（210 $\times$ 297 mm $\doteq$ 595 $\times$ 842 pt）
最终输出指定名称的 pdf，所有页面尺寸统一为 A4，便于打印或归档
## 🚀 快速开始
### 1. 克隆 / 下载
```powershell
git clone https://github.com/maohy0/merge-pdf-tool.git
cd merge-pdf-tool
```
### 2. 安装依赖
仅需 pypdf（>= 3.0）：
```bash
pip install pypdf
```
### 3. 放入 PDF
把需要合并的 PDF 直接放到脚本所在目录。
### 4. 运行
```bash
python pdfmerge.py
```
脚本会自动删除旧 pdf（防止重复合并），然后生成新的 pdf 并提示总页数
