from lib.base import BaseGithubAction

__all__ = [
    'DisableAutomatedSecurityFixesAction'
]


class DisableAutomatedSecurityFixesAction(BaseGithubAction):
    def run(self, user, repo):
        user = self._client.get_user(user)
        repo = user.get_repo(repo)
        result = repo.disable_automated_security_fixes()
        return result
