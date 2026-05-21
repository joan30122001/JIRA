import os
import requests
from requests.auth import HTTPBasicAuth


class TestRailService:
    def __init__(self):
        self.base_url = os.getenv("TESTRAIL_BASE_URL", "").strip().rstrip("/")
        self.username = os.getenv("TESTRAIL_USERNAME", "").strip()
        self.api_key = os.getenv("TESTRAIL_API_KEY", "").strip()

        if not self.base_url or not self.username or not self.api_key:
            raise ValueError(
                "Config TestRail manquante: TESTRAIL_BASE_URL, "
                "TESTRAIL_USERNAME, TESTRAIL_API_KEY"
            )

        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.auth = HTTPBasicAuth(self.username, self.api_key)

    def request(self, method, endpoint, payload=None):
        url = f"{self.base_url}/index.php?/api/v2/{endpoint}"

        response = requests.request(
            method=method,
            url=url,
            headers=self.headers,
            auth=self.auth,
            json=payload,
            timeout=30,
        )

        print("TESTRAIL METHOD:", method)
        print("TESTRAIL URL:", url)
        print("TESTRAIL PAYLOAD:", payload)
        print("TESTRAIL STATUS:", response.status_code)
        print("TESTRAIL RESPONSE:", response.text)

        if response.status_code >= 400:
            raise requests.HTTPError(
                f"TestRail error {response.status_code}",
                response=response,
            )

        return response.json() if response.text else {}

    def get_projects(self):
        return self.request("GET", "get_projects")

    def get_project(self, project_id):
        return self.request("GET", f"get_project/{project_id}")

    def add_project(self, name, announcement="", show_announcement=True, suite_mode=1):
        payload = {
            "name": name,
            "announcement": announcement,
            "show_announcement": show_announcement,
            "suite_mode": suite_mode,
        }
        return self.request("POST", "add_project", payload)

    def get_suites(self, project_id):
        return self.request("GET", f"get_suites/{project_id}")

    def add_milestone(self, project_id, name, description="", start_on=None, due_on=None):
        payload = {
            "name": name,
            "description": description,
        }
        if start_on is not None:
            payload["start_on"] = start_on
        if due_on is not None:
            payload["due_on"] = due_on
        return self.request("POST", f"add_milestone/{project_id}", payload)

    def add_section(self, project_id, name, description="", suite_id=None):
        payload = {
            "name": name,
            "description": description,
        }
        if suite_id is not None:
            payload["suite_id"] = suite_id
        return self.request("POST", f"add_section/{project_id}", payload)

    def add_case(self, section_id, title, steps="", expected="", refs=None, priority_id=None):
        payload = {
            "title": title,
            "custom_steps_separated": [
                {
                    "content": steps,
                    "expected": expected,
                }
            ]
        }
        if refs is not None:
            payload["refs"] = refs
        if priority_id is not None:
            payload["priority_id"] = priority_id

        return self.request("POST", f"add_case/{section_id}", payload)

    def update_case(self, case_id, title=None, steps=None, expected=None, refs=None, priority_id=None):
        payload = {}

        if title is not None:
            payload["title"] = title
        if refs is not None:
            payload["refs"] = refs
        if priority_id is not None:
            payload["priority_id"] = priority_id
        if steps is not None or expected is not None:
            payload["custom_steps_separated"] = [
                {
                    "content": steps or "",
                    "expected": expected or "",
                }
            ]

        return self.request("POST", f"update_case/{case_id}", payload)

    def get_statuses(self):
        return self.request("GET", "get_statuses")

    def add_run(self, project_id, suite_id, name, description="", include_all=True, case_ids=None, milestone_id=None):
        payload = {
            "suite_id": suite_id,
            "name": name,
            "description": description,
            "include_all": include_all,
        }
        if not include_all and case_ids:
            payload["case_ids"] = case_ids
        if milestone_id is not None:
            payload["milestone_id"] = milestone_id

        return self.request("POST", f"add_run/{project_id}", payload)

    def get_run(self, run_id):
        return self.request("GET", f"get_run/{run_id}")

    def close_run(self, run_id):
        return self.request("POST", f"close_run/{run_id}", {})

    def delete_run(self, run_id):
        return self.request("POST", f"delete_run/{run_id}", {})

    def add_plan(self, project_id, name, description="", milestone_id=None):
        payload = {
            "name": name,
            "description": description,
        }
        if milestone_id is not None:
            payload["milestone_id"] = milestone_id

        return self.request("POST", f"add_plan/{project_id}", payload)

    def get_plan(self, plan_id):
        return self.request("GET", f"get_plan/{plan_id}")

    def close_plan(self, plan_id):
        return self.request("POST", f"close_plan/{plan_id}", {})

    def delete_plan(self, plan_id):
        return self.request("POST", f"delete_plan/{plan_id}", {})

    def add_plan_entry(self, plan_id, suite_id, name, description="", include_all=True, case_ids=None, milestone_id=None):
        payload = {
            "suite_id": suite_id,
            "name": name,
            "description": description,
            "include_all": include_all,
        }
        if not include_all and case_ids:
            payload["case_ids"] = case_ids
        if milestone_id is not None:
            payload["milestone_id"] = milestone_id

        return self.request("POST", f"add_plan_entry/{plan_id}", payload)

    def add_result_for_case(self, run_id, case_id, status_id, comment="", version=None, defects=None, elapsed=None):
        payload = {
            "status_id": status_id,
            "comment": comment,
        }
        if version is not None:
            payload["version"] = version
        if defects is not None:
            payload["defects"] = defects
        if elapsed is not None:
            payload["elapsed"] = elapsed

        return self.request("POST", f"add_result_for_case/{run_id}/{case_id}", payload)

    def add_results_for_cases(self, run_id, results):
        payload = {"results": results}
        return self.request("POST", f"add_results_for_cases/{run_id}", payload)