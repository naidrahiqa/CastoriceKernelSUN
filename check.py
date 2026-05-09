import urllib.request, json
data = json.loads(urllib.request.urlopen('https://api.github.com/repos/naidrahiqa/CastoriceKernelSUN/actions/runs?per_page=1').read())
run_id = data['workflow_runs'][0]['id']
print("Run ID:", run_id)
jobs = json.loads(urllib.request.urlopen(f'https://api.github.com/repos/naidrahiqa/CastoriceKernelSUN/actions/runs/{run_id}/jobs').read())
for j in jobs['jobs']:
    if j['conclusion'] == 'failure':
        print(j['name'])
        # Try to download the logs for this job
        try:
            log_url = f"https://api.github.com/repos/naidrahiqa/CastoriceKernelSUN/actions/jobs/{j['id']}/logs"
            req = urllib.request.Request(log_url)
            log = urllib.request.urlopen(req).read().decode('utf-8', errors='replace')
            print("\nLAST 50 LINES OF LOG:")
            print("\n".join(log.splitlines()[-50:]))
            print("-" * 50)
        except Exception as e:
            print("Failed to download logs:", e)
