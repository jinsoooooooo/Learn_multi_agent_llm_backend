from pathlib import Path

# 제외할 폴더/파일 목록
EXCLUDE = {".venv", "__pycache__", ".ipynb_checkpoints", ".DS_Store", ".pytest_cache"}

def print_md_tree(path: Path, prefix=""):
    """프로젝트 관련 파일만 Markdown 스타일로 트리 출력"""
    if prefix == "":
        print(f"{path.name}/")
    
    # 정렬: 디렉토리 먼저, 그 다음 파일
    items = sorted([i for i in path.iterdir() if i.name not in EXCLUDE],
                   key=lambda x: (x.is_file(), x.name))
    
    for i, item in enumerate(items):
        connector = "└─" if i == len(items) - 1 else "├─"
        if item.is_dir():
            print(f"{prefix}{connector} {item.name}/")
            print_md_tree(item, prefix + ("   " if i == len(items) - 1 else "│  "))
        else:
            print(f"{prefix}{connector} {item.name}")

# 사용
project_root = Path(".")  # 현재 프로젝트 루트 기준
print_md_tree(project_root)
