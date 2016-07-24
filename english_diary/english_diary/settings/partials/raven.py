import os

import raven


RAVEN_CONFIG = {
    'dsn': os.environ.get("DSN"),
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    # 'release': raven.fetch_git_sha(os.path.dirname(__file__)),
}
