from .safe_call import safe_call

def main(args):
    safe_call('gcloud', 'dataproc', 'clusters', 'list')
