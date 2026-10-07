import importlib.util, pathlib
import pandas as pd
_spec = importlib.util.spec_from_file_location('reg', pathlib.Path(__file__).with_name('03_registered.py'))
reg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(reg)
for h in reg.HYPOTHESES:
    print(h)
    print("---")
print("build_formula sig:", reg.build_formula.__doc__)
print("fit sig:", reg.fit.__doc__)
