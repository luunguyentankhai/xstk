from pathlib import Path
import os
import kagglehub
import shutil
import stat

def Pulldata():
    try:
        Base_dir = Path(__file__).resolve().parent.parent

        Path_Install = Path(Base_dir / "data" / "raw")

        Path_Install.mkdir(parents=True, exist_ok=True)
        
        Cache_path = Path(kagglehub.dataset_download("afumetto/3dprinter"))

        for csv_file in Cache_path.rglob('*.csv'):
            target = Path_Install / csv_file.name

            if target.exists():
                target.chmod(target.stat().st_mode | stat.S_IWRITE)

            shutil.copyfile(csv_file, target)
            target.chmod(target.stat().st_mode | stat.S_IWRITE)
            
    except Exception as e:
        print(f"Error : {e}")
    finally:
        pass

