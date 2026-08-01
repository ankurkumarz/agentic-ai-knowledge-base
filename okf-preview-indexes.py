import importlib.util
spec = importlib.util.spec_from_file_location("gen", "scripts/generate-okf-indexes.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

for d in ["AgentHarness", "Standards", "ProductionBestPractices", "AllThingsAWS"]:
    print("=== " + d + " ===")
    print(mod.generate_index(mod.DOCS / d))
    print()
