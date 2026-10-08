import importlib.util, pathlib
_spec = importlib.util.spec_from_file_location('reg', pathlib.Path(__file__).with_name('03_registered.py'))
reg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(reg)

import pandas as pd

pathlib.Path('results').mkdir(exist_ok=True)
d = pd.read_csv('data/clean.csv')
for c in ['treatment', 'toward_counterarg', 'certainty', 'counterarg_keyword', 'supportive_keyword']:
    d[c] = pd.to_numeric(d[c], errors='coerce')

H = {(h.get('id') or h.get('analysis_id')): h for h in reg.HYPOTHESES}


def treat_row(df):
    m = df[df['term'].astype(str).str.contains('treat')]
    return (m if len(m) else df.tail(1)).iloc[0]


# E1: Robustness of H1 (movement toward op-ed) to restricting to the pro-spending group,
# the majority group, with the registered specification held fixed.
full = reg.reestimate(H['H1'], d).assign(sample='full')
sub = reg.reestimate(H['H1'], d[d['group'] == 'pro']).assign(sample='pro-spending only')
e1 = pd.concat([full, sub], ignore_index=True)
e1.insert(0, 'analysis', 'E1')
e1.to_csv('results/E1_h1_pro_only_robustness.csv', index=False)
r_full, r_sub = treat_row(full), treat_row(sub)
print(f"E1 H1 robustness to pro-spending-only sample: effect {r_sub['estimate']:.3f} "
      f"(SE {r_sub['std_error']:.3f}, p={r_sub['p_value']:.3g}, n={int(r_sub['n'])}) versus full-sample "
      f"{r_full['estimate']:.3f} (SE {r_full['std_error']:.3f}); 1 restricted re-estimate of 1 planned test.")

# E2: Heterogeneity of H3 (counterargument keyword recall) by group, as a text moderator.
e2 = reg.reestimate(H['H3'], d, moderator='group')
e2.insert(0, 'analysis', 'E2')
e2.to_csv('results/E2_h3_by_group.csv', index=False)
lvl = next((c for c in ['level', 'moderator_level', 'group'] if c in e2.columns), None)
parts = []
for _, r in e2.iterrows():
    name = r[lvl] if lvl else ''
    if 'estimate' in r and pd.notna(r['estimate']):
        parts.append(f"{name}: {r['estimate']:.3f} (SE {r['std_error']:.3f}, p={r['p_value']:.2g})")
print("E2 H3 counterargument keyword effect by group (2 groups tested, interaction not tested): "
      + "; ".join(parts))
