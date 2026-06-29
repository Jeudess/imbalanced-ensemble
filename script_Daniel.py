files = [
    'imbens/pipeline.py',
    'imbens/sampler/base.py',
    'imbens/sampler/_over_sampling/_adasyn.py',
    'imbens/sampler/_over_sampling/_random_over_sampler.py',
    'imbens/sampler/_over_sampling/_smote/filter.py',
]

for path in files:
    with open(path, encoding='utf-8-sig') as f:
        content = f.read()
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'BOM removido: {path}')