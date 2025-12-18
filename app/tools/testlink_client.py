from testlink import TestlinkAPIClient
from app.models import Project, Step


# class TestLinkConnector:
#     def __init__(self, url, dev_key, jira_key):
#         self.tlc = TestlinkAPIClient(url, dev_key)
#         self.project_name = jira_key  # Nom du projet dans TestLink basé sur la clé Jira
#         self.test_plan_name = "DemoPlan"
#         self.test_case_name = "Test Case 1"
#         self.build_name = "Build 1"
#         self.username = "admin"
#         self.project_id = self.get_or_create_project()

#     def get_or_create_project(self):
#         for project in self.tlc.getProjects():
#             if project["name"] == self.project_name:
#                 return int(project["id"])
#         created = self.tlc.createTestProject(
#             testprojectname=self.project_name,
#             testcaseprefix=self.project_name[:4].upper(),
#             notes="Projet auto",
#             enableRequirements=True,
#             enableTestPriority=True,
#             enableAutomation=True,
#             enableInventory=False
#         )
#         return int(created["id"]) if isinstance(created, dict) else int(created[0]["id"])

#     def create_test_plan_if_not_exist(self):
#         for plan in self.tlc.getProjectTestPlans(self.project_id):
#             if plan["name"] == self.test_plan_name:
#                 return int(plan["id"])
#         created = self.tlc.createTestPlan(
#             testprojectname=self.project_name,
#             testplanname=self.test_plan_name,
#             notes="Plan auto",
#             active=1,
#             public=1
#         )
#         return int(created["id"]) if isinstance(created, dict) else int(created[0]["id"])

#     def create_test_suite_if_not_exist(self):
#         try:
#             suites = self.tlc.getFirstLevelTestSuitesForTestProject(self.project_id)
#             if isinstance(suites, list) and suites and "id" in suites[0]:
#                 return int(suites[0]["id"])
#         except:
#             pass
#         created = self.tlc.createTestSuite(
#             self.project_id,
#             "Suite Django",
#             "Suite créée automatiquement"
#         )
#         return int(created["id"])

#     def create_test_case_if_not_exist(self, suite_id):
#         cases = self.tlc.getTestCasesForTestSuite(suite_id, True, "full")

#         if isinstance(cases, dict):
#             for case_group in cases.values():
#                 if isinstance(case_group, list):
#                     for case in case_group:
#                         if isinstance(case, dict) and case.get("name") == self.test_case_name:
#                             return case.get("external_id")

#         elif isinstance(cases, list):
#             for case in cases:
#                 if isinstance(case, dict) and case.get("name") == self.test_case_name:
#                     return case.get("external_id")

#         created = self.tlc.createTestCase(
#             testcasename=self.test_case_name,
#             testsuiteid=suite_id,
#             testprojectid=self.project_id,
#             authorlogin=self.username,
#             summary="Étapes de test automatisé",
#             steps="Étape 1 → Résultat attendu"
#         )
#         case_id = int(created["id"]) if isinstance(created, dict) else int(created[0]["id"])
#         case_info = self.tlc.getTestCase(case_id)

#         if isinstance(case_info, list) and case_info:
#             return case_info[0].get("external_id")

#         raise Exception("Test case external_id not found")

#     def create_build_if_not_exist(self, plan_id):
#         builds = self.tlc.getBuildsForTestPlan(plan_id)
#         for build in builds:
#             if build["name"] == self.build_name:
#                 return build["name"]
#         created = self.tlc.createBuild(
#             testplanid=plan_id,
#             buildname=self.build_name,
#             buildnotes="Build auto"
#         )
#         return created["name"] if isinstance(created, dict) else self.build_name

#     def add_case_to_plan_if_needed(self, testcase_external_id, test_plan_id):
#         try:
#             self.tlc.addTestCaseToTestPlan(
#                 testprojectid=self.project_id,
#                 testplanid=test_plan_id,
#                 testcaseexternalid=testcase_external_id,
#                 version=1
#             )
#         except Exception as e:
#             if "already linked" in str(e).lower():
#                 pass
#             else:
#                 raise e

#     def report_result(self, status="p"):
#         test_plan_id = self.create_test_plan_if_not_exist()
#         suite_id = self.create_test_suite_if_not_exist()
#         case_external_id = self.create_test_case_if_not_exist(suite_id)
#         build_name = self.create_build_if_not_exist(test_plan_id)

#         self.add_case_to_plan_if_needed(case_external_id, test_plan_id)

#         result = self.tlc.reportTCResult(
#             testcaseexternalid=case_external_id,
#             testplanid=test_plan_id,
#             buildname=build_name,
#             status=status
#         )
#         return result




class TestLinkConnector:
    def __init__(self, url, dev_key, jira_key, test_plan_name):
        self.tlc = TestlinkAPIClient(url, dev_key)
        self.project_name = jira_key
        self.test_plan_name = test_plan_name
        self.build_name = "Build 1"
        self.username = "admin"
        self.project_id = self.get_or_create_project()

    def get_or_create_project(self):
        for project in self.tlc.getProjects():
            if project["name"] == self.project_name:
                return int(project["id"])
        created = self.tlc.createTestProject(
            testprojectname=self.project_name,
            testcaseprefix=self.project_name[:4].upper(),
            notes="Projet auto",
            enableRequirements=True,
            enableTestPriority=True,
            enableAutomation=True,
            enableInventory=False
        )
        return int(created["id"]) if isinstance(created, dict) else int(created[0]["id"])

    def create_test_plan_if_not_exist(self):
        for plan in self.tlc.getProjectTestPlans(self.project_id):
            if plan["name"] == self.test_plan_name:
                return int(plan["id"])
        created = self.tlc.createTestPlan(
            testprojectname=self.project_name,
            testplanname=self.test_plan_name,
            notes="Plan auto",
            active=1,
            public=1
        )
        return int(created["id"]) if isinstance(created, dict) else int(created[0]["id"])

    def create_test_suite_if_not_exist(self):
        try:
            suites = self.tlc.getFirstLevelTestSuitesForTestProject(self.project_id)
            if isinstance(suites, list) and suites and "id" in suites[0]:
                return int(suites[0]["id"])
        except:
            pass
        created = self.tlc.createTestSuite(
            self.project_id,
            "Suite Django",
            "Suite créée automatiquement"
        )
        return int(created["id"])

    def create_build_if_not_exist(self, plan_id):
        builds = self.tlc.getBuildsForTestPlan(plan_id)
        for build in builds:
            if build["name"] == self.build_name:
                return build["name"]
        created = self.tlc.createBuild(
            testplanid=plan_id,
            buildname=self.build_name,
            buildnotes="Build auto"
        )
        return created["name"] if isinstance(created, dict) else self.build_name

    def add_case_to_plan_if_needed(self, testcase_external_id, test_plan_id):
        try:
            self.tlc.addTestCaseToTestPlan(
                testprojectid=self.project_id,
                testplanid=test_plan_id,
                testcaseexternalid=testcase_external_id,
                version=1
            )
        except Exception as e:
            if "already linked" in str(e).lower():
                pass
            else:
                raise e

    def create_test_cases_from_project(self):
        try:
            project = Project.objects.get(key=self.project_name)
        except Project.DoesNotExist:
            raise Exception("Projet non trouvé dans la base Django")

        steps = Step.objects.filter(project=project)
        if not steps.exists():
            raise Exception("Aucune étape trouvée pour ce projet")

        suite_id = self.create_test_suite_if_not_exist()
        test_plan_id = self.create_test_plan_if_not_exist()

        for step in steps:
            created = self.tlc.createTestCase(
                testcasename=step.title,
                testsuiteid=suite_id,
                testprojectid=self.project_id,
                authorlogin=self.username,
                summary=step.description or "Pas de description",
                steps=step.description or "Pas de description"
            )

            case_id = int(created["id"]) if isinstance(created, dict) else int(created[0]["id"])
            case_info = self.tlc.getTestCase(case_id)

            # ✅ Fix ici : extraction robuste de l'external_id
            if isinstance(case_info, list) and case_info:
                case_data = case_info[0]
                case_external_id = case_data.get("external_id") or case_data.get("full_tc_external_id")
                if not case_external_id:
                    raise Exception("Test case external_id introuvable")
            else:
                raise Exception("Test case non trouvé ou réponse vide")

            self.add_case_to_plan_if_needed(case_external_id, test_plan_id)

        return test_plan_id

    # def report_result(self, status="p"):
    #     test_plan_id = self.create_test_cases_from_project()
    #     build_name = self.create_build_if_not_exist(test_plan_id)

    #     suites = self.tlc.getFirstLevelTestSuitesForTestProject(self.project_id)
    #     if not suites:
    #         raise Exception("Aucune suite trouvée pour ce projet")

    #     cases = self.tlc.getTestCasesForTestSuite(suites[0]['id'], True, "full")

    #     if isinstance(cases, dict):
    #         for case_group in cases.values():
    #             for case in case_group:
    #                 case_external_id = case.get("external_id") or case.get("full_tc_external_id")
    #                 if not case_external_id:
    #                     continue
    #                 self.tlc.reportTCResult(
    #                     testcaseexternalid=case_external_id,
    #                     testplanid=test_plan_id,
    #                     buildname=build_name,
    #                     status=status
    #                 )

    def report_result(self, status="p"):
        test_plan_id = self.create_test_cases_from_project()
        build_name = self.create_build_if_not_exist(test_plan_id)

        suites = self.tlc.getFirstLevelTestSuitesForTestProject(self.project_id)
        if not suites:
            raise Exception("Aucune suite trouvée pour ce projet")

        for suite in suites:
            cases = self.tlc.getTestCasesForTestSuite(suite['id'], True, "full")
            if isinstance(cases, dict):
                for case_group in cases.values():
                    for case in case_group:
                        case_external_id = case.get("external_id") or case.get("full_tc_external_id")
                        if not case_external_id:
                            continue
                        self.tlc.reportTCResult(
                            testcaseexternalid=case_external_id,
                            testplanid=test_plan_id,
                            buildname=build_name,
                            status=status
                        )