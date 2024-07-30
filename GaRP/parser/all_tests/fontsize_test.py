from pathlib import Path
from typing import Iterable, Any

from pdfminer.high_level import extract_pages


def show_ltitem_hierarchy(o: Any, depth=0):
    """Show location and text of LTItem and all its descendants"""
    if depth == 0:
        print('element                        font                  stroking color  text')
        print('------------------------------ --------------------- --------------  ----------')

    if hasattr(o, 'size') and round(o.size) != 12:  # Überprüfe, ob die Schriftgröße nicht 12 pt ist
        print(
            f'{get_indented_name(o, depth):<30.30s} '
            f'{get_optional_fontinfo(o):<20.20s} '
            f'{get_optional_color(o):<17.17s}'
            f'{get_optional_text(o)}'
        )

    if isinstance(o, Iterable):
        for i in o:
            show_ltitem_hierarchy(i, depth=depth + 1)


def get_indented_name(o: Any, depth: int) -> str:
    """Indented name of class"""
    return '  ' * depth + o.__class__.__name__

def get_optional_fontinfo(o: Any) -> str:
    """Font info of LTChar if available, otherwise empty string"""
    if hasattr(o, 'fontname') and hasattr(o, 'size'):
        return f'{o.fontname} {round(o.size)}pt'
    return ''

def get_optional_color(o: Any) -> str:
    """Font info of LTChar if available, otherwise empty string"""
    if hasattr(o, 'graphicstate'):
        return f'{o.graphicstate.scolor}'
    return ''


def get_optional_text(o: Any) -> str:
    """Text of LTItem if available, otherwise empty string"""
    if hasattr(o, 'get_text'):
        return o.get_text().strip()
    return ''


path = Path('C:\Visual Studio Code\VSC\Sonstiges\pdf_parser\TestDokument.pdf').expanduser()
pages = extract_pages(path)
show_ltitem_hierarchy(pages)