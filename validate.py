import yaml
with open(".github/workflows/build.yml") as f:
    wf = yaml.safe_load(f)
print("Name:", wf["name"])
print("Trigger:", list(wf["on"].keys()))
print("Jobs:", list(wf["jobs"].keys()))
steps = wf["jobs"]["build"]["steps"]
print("Steps:", len(steps))
for i, s in enumerate(steps):
    print("  {}. {}".format(i+1, s["name"]))
print("ALL GOOD")
