"""
从当前文件夹读取所有 PDF -> 按文件名排序 -> 合并 -> 每页统一 A4
"""

from pathlib import Path
from pypdf import PdfReader, PdfWriter, PageObject, Transformation

# A4纸尺寸，单位为pt, 1 inch = 72 pt
A4_WIDTH_PT  = 595  # 210 mm
A4_HEIGHT_PT = 842  # 297 mm

# 目标合并成的文件名
f = "certs.pdf"

def resize_page2a4(page: PageObject) -> PageObject:
    """
    将传入的任意页面等比缩放到 A4 大小，并居中放置
    返回新的 A4 页面对象
    """
    # 获取原始页面的宽高
    src_w = float(page.mediabox.width)
    src_h = float(page.mediabox.height)

    # 计算缩放比例（取最小防止溢出和变形）
    scale = min(A4_WIDTH_PT / src_w, A4_HEIGHT_PT / src_h)

    # 计算居中平移量
    tx = (A4_WIDTH_PT  - src_w * scale) / 2
    ty = (A4_HEIGHT_PT - src_h * scale) / 2

    # 先新建一张空白 A4 页面
    new_page = PageObject.create_blank_page(width=A4_WIDTH_PT, height=A4_HEIGHT_PT)

    # 把原页面内容缩放、居中，合并到新页面
    new_page.merge_transformed_page(
        page,
        Transformation().scale(scale, scale).translate(tx, ty)
    )
    return new_page


def merge_folder_pdfs(folder: Path, out_file: Path = Path(f)) -> None:
    pdf_files = sorted(folder.glob("*.pdf"))    # 按字符顺序排列，生成一个列表
    if not pdf_files:
        raise FileNotFoundError("目录内未找到 PDF 文件")

    writer = PdfWriter()
    for pdf_path in pdf_files:
        reader = PdfReader(pdf_path)    # 读取每个文件
        for page in reader.pages:
            writer.add_page(resize_page2a4(page))   # 每一页先转a4然后加进去

    writer.write(out_file)  # 直接用默认值
    print(f"合并完成 -> {out_file.resolve()}  (共 {len(writer.pages)} 页)")


if __name__ == "__main__":
    original_pdf = Path(f)
    original_pdf.unlink(missing_ok=True)  # 删除原来的pdf文件，防止套娃，看着有点类似删Linux的软连接的方法，missing_ok参数让程序找不到certs.pdf也不会报错
    merge_folder_pdfs(Path(__file__).parent)   # 默认脚本所在目录