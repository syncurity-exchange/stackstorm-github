from lib.base import BaseGithubAction

__all__ = [
    'EnableAutomatedSecurityFixesAction'
]


class EnableAutomatedSecurityFixesAction(BaseGithubAction):
    def run(self, user, repo):
        user = self._client.get_user(user)
        repo = user.get_repo(repo)
        result = repo.enable_automated_security_fixes()
        return result
