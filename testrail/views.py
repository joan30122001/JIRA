# from django.http import JsonResponse
# from django.views.decorators.http import require_http_methods
# from .services.testrail_service import TestRailService
# import json


# def parse_body(request):
#     try:
#         return json.loads(request.body.decode("utf-8")) if request.body else {}
#     except Exception:
#         return {}


# @require_http_methods(["GET"])
# def testrail_projects(request):
#     try:
#         service = TestRailService()
#         data = service.get_projects()
#         return JsonResponse(data, safe=False)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)


# @require_http_methods(["POST"])
# def testrail_create_project(request):
#     try:
#         body = parse_body(request)
#         service = TestRailService()

#         project = service.add_project(
#             name=body.get("name", ""),
#             announcement=body.get("announcement", ""),
#             show_announcement=body.get("show_announcement", True),
#             suite_mode=body.get("suite_mode", 1),
#         )
#         return JsonResponse(project, status=201)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)


# @require_http_methods(["POST"])
# def testrail_create_milestone(request, project_id):
#     try:
#         body = parse_body(request)
#         service = TestRailService()

#         milestone = service.add_milestone(
#             project_id=project_id,
#             name=body.get("name", ""),
#             description=body.get("description", ""),
#             start_on=body.get("start_on"),
#             due_on=body.get("due_on"),
#         )
#         return JsonResponse(milestone, status=201)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)


# @require_http_methods(["GET"])
# def testrail_suites(request, project_id):
#     try:
#         service = TestRailService()
#         data = service.get_suites(project_id)
#         return JsonResponse(data, safe=False)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)


# @require_http_methods(["POST"])
# def testrail_create_section(request, project_id):
#     try:
#         body = parse_body(request)
#         service = TestRailService()

#         section = service.add_section(
#             project_id=project_id,
#             name=body.get("name", ""),
#             description=body.get("description", ""),
#             suite_id=body.get("suite_id"),
#         )
#         return JsonResponse(section, status=201)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)


# @require_http_methods(["POST"])
# def testrail_create_case(request, section_id):
#     try:
#         body = parse_body(request)
#         service = TestRailService()

#         case = service.add_case(
#             section_id=section_id,
#             title=body.get("title", ""),
#             steps=body.get("steps", ""),
#             expected=body.get("expected", ""),
#             refs=body.get("refs"),
#             priority_id=body.get("priority_id"),
#         )
#         return JsonResponse(case, status=201)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)


# @require_http_methods(["POST"])
# def testrail_update_case(request, case_id):
#     try:
#         body = parse_body(request)
#         service = TestRailService()

#         case = service.update_case(
#             case_id=case_id,
#             title=body.get("title"),
#             steps=body.get("steps"),
#             expected=body.get("expected"),
#             refs=body.get("refs"),
#             priority_id=body.get("priority_id"),
#         )
#         return JsonResponse(case, status=200)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)


# @require_http_methods(["GET"])
# def testrail_statuses(request):
#     try:
#         service = TestRailService()
#         data = service.get_statuses()
#         return JsonResponse(data, safe=False)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)


# @require_http_methods(["POST"])
# def testrail_create_run(request, project_id):
#     try:
#         body = parse_body(request)
#         service = TestRailService()

#         run = service.add_run(
#             project_id=project_id,
#             suite_id=body.get("suite_id"),
#             name=body.get("name", ""),
#             description=body.get("description", ""),
#             include_all=body.get("include_all", True),
#             case_ids=body.get("case_ids"),
#             milestone_id=body.get("milestone_id"),
#         )
#         return JsonResponse(run, status=201)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)


# @require_http_methods(["POST"])
# def testrail_close_run(request, run_id):
#     try:
#         service = TestRailService()
#         data = service.close_run(run_id)
#         return JsonResponse(data, safe=False)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)


# @require_http_methods(["POST"])
# def testrail_create_plan(request, project_id):
#     try:
#         body = parse_body(request)
#         service = TestRailService()

#         plan = service.add_plan(
#             project_id=project_id,
#             name=body.get("name", ""),
#             description=body.get("description", ""),
#             milestone_id=body.get("milestone_id"),
#         )
#         return JsonResponse(plan, status=201)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)


# @require_http_methods(["POST"])
# def testrail_add_plan_entry(request, plan_id):
#     try:
#         body = parse_body(request)
#         service = TestRailService()

#         entry = service.add_plan_entry(
#             plan_id=plan_id,
#             suite_id=body.get("suite_id"),
#             name=body.get("name", ""),
#             description=body.get("description", ""),
#             include_all=body.get("include_all", True),
#             case_ids=body.get("case_ids"),
#             milestone_id=body.get("milestone_id"),
#         )
#         return JsonResponse(entry, status=201)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)


# @require_http_methods(["POST"])
# def testrail_add_result(request, run_id, case_id):
#     try:
#         body = parse_body(request)
#         service = TestRailService()

#         result = service.add_result_for_case(
#             run_id=run_id,
#             case_id=case_id,
#             status_id=body.get("status_id"),
#             comment=body.get("comment", ""),
#             version=body.get("version"),
#             defects=body.get("defects"),
#             elapsed=body.get("elapsed"),
#         )
#         return JsonResponse(result, status=201)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)


# @require_http_methods(["POST"])
# def testrail_add_bulk_results(request, run_id):
#     try:
#         body = parse_body(request)
#         service = TestRailService()

#         result = service.add_results_for_cases(
#             run_id=run_id,
#             results=body.get("results", []),
#         )
#         return JsonResponse(result, status=201)
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=400)






import os
import json
import requests
from django.shortcuts import render
from requests.auth import HTTPBasicAuth


def testrail_request(method, endpoint, payload=None):
    base_url = os.getenv("TESTRAIL_BASE_URL", "").strip().rstrip("/")
    username = os.getenv("TESTRAIL_USERNAME", "").strip()
    api_key = os.getenv("TESTRAIL_API_KEY", "").strip()

    if not base_url or not username or not api_key:
        raise ValueError(
            f"Config TestRail manquante | "
            f"TESTRAIL_BASE_URL={base_url or 'vide'} | "
            f"TESTRAIL_USERNAME={username or 'vide'} | "
            f"TESTRAIL_API_KEY={'présent' if api_key else 'vide'}"
        )

    url = f"{base_url}/index.php?/api/v2/{endpoint}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    response = requests.request(
        method=method,
        url=url,
        headers=headers,
        auth=HTTPBasicAuth(username, api_key),
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
            response=response
        )

    return response.json() if response.text else {}


def parse_request_data(request):
    if request.content_type == "application/json":
        try:
            return json.loads(request.body.decode("utf-8")) if request.body else {}
        except Exception:
            return {}
    return request.POST


def build_context(title, action_url=None, extra=None):
    ctx = {
        "title": title,
        "action_url": action_url,
        "success": "",
        "error": "",
        "result": None,
        "results": None,
    }
    if extra:
        ctx.update(extra)
    return ctx


def handle_http_error(ctx, e):
    response = getattr(e, "response", None)
    status_code = response.status_code if response is not None else "N/A"
    response_text = response.text if response is not None else "Aucune réponse"
    request_url = response.url if response is not None else "URL inconnue"

    ctx["error"] = (
        f"Erreur TestRail | "
        f"type={type(e).__name__} | "
        f"status={status_code} | "
        f"url={request_url} | "
        f"response={response_text}"
    )
    return ctx


def testrail_projects(request):
    ctx = build_context("TestRail Projects")
    try:
        data = testrail_request("GET", "get_projects")
        ctx["result"] = data
        ctx["projects"] = data.get("projects", []) if isinstance(data, dict) else data
    except requests.HTTPError as e:
        handle_http_error(ctx, e)
    except Exception as e:
        ctx["error"] = str(e)
    return render(request, "testrail/projects_list.html", ctx)


def testrail_create_project(request):
    ctx = build_context("Create TestRail Project", action_url=request.path)

    if request.method == "POST":
        data = parse_request_data(request)
        payload = {
            "name": data.get("name", ""),
            "announcement": data.get("announcement", ""),
            "show_announcement": True if str(data.get("show_announcement", "true")).lower() in ["true", "1", "on", "yes"] else False,
            "suite_mode": int(data.get("suite_mode", 1)),
        }

        try:
            result = testrail_request("POST", "add_project", payload)
            ctx["success"] = "Projet TestRail créé avec succès."
            ctx["result"] = result
        except requests.HTTPError as e:
            handle_http_error(ctx, e)
        except Exception as e:
            ctx["error"] = str(e)

    return render(request, "testrail/project_form.html", ctx)


def testrail_create_milestone(request, project_id):
    ctx = build_context("Create Milestone", action_url=request.path, extra={"project_id": project_id})

    if request.method == "POST":
        data = parse_request_data(request)
        payload = {
            "name": data.get("name", ""),
            "description": data.get("description", ""),
        }

        start_on = data.get("start_on")
        due_on = data.get("due_on")

        if start_on:
            payload["start_on"] = int(start_on)
        if due_on:
            payload["due_on"] = int(due_on)

        try:
            result = testrail_request("POST", f"add_milestone/{project_id}", payload)
            ctx["success"] = "Milestone créée avec succès."
            ctx["result"] = result
        except requests.HTTPError as e:
            handle_http_error(ctx, e)
        except Exception as e:
            ctx["error"] = str(e)

    return render(request, "testrail/milestone_form.html", ctx)


def testrail_suites(request, project_id):
    ctx = build_context("Project Suites", extra={"project_id": project_id})
    try:
        data = testrail_request("GET", f"get_suites/{project_id}")
        ctx["result"] = data
        ctx["suites"] = data if isinstance(data, list) else data.get("suites", [])
    except requests.HTTPError as e:
        handle_http_error(ctx, e)
    except Exception as e:
        ctx["error"] = str(e)
    return render(request, "testrail/suites_list.html", ctx)


def testrail_create_section(request, project_id):
    ctx = build_context("Create Section", action_url=request.path, extra={"project_id": project_id})

    if request.method == "POST":
        data = parse_request_data(request)
        payload = {
            "name": data.get("name", ""),
            "description": data.get("description", ""),
        }

        suite_id = data.get("suite_id")
        if suite_id:
            payload["suite_id"] = int(suite_id)

        try:
            result = testrail_request("POST", f"add_section/{project_id}", payload)
            ctx["success"] = "Section créée avec succès."
            ctx["result"] = result
        except requests.HTTPError as e:
            handle_http_error(ctx, e)
        except Exception as e:
            ctx["error"] = str(e)

    return render(request, "testrail/section_form.html", ctx)


def testrail_create_run(request, project_id):
    ctx = build_context("Create Run", action_url=request.path, extra={"project_id": project_id})

    if request.method == "POST":
        data = parse_request_data(request)

        include_all = True if str(data.get("include_all", "true")).lower() in ["true", "1", "on", "yes"] else False

        payload = {
            "suite_id": int(data.get("suite_id")),
            "name": data.get("name", ""),
            "description": data.get("description", ""),
            "include_all": include_all,
        }

        milestone_id = data.get("milestone_id")
        case_ids = data.get("case_ids", "")

        if milestone_id:
            payload["milestone_id"] = int(milestone_id)

        if not include_all and case_ids:
            payload["case_ids"] = [int(x.strip()) for x in case_ids.split(",") if x.strip()]

        try:
            result = testrail_request("POST", f"add_run/{project_id}", payload)
            ctx["success"] = "Run créé avec succès."
            ctx["result"] = result
        except requests.HTTPError as e:
            handle_http_error(ctx, e)
        except Exception as e:
            ctx["error"] = str(e)

    return render(request, "testrail/run_form.html", ctx)


def testrail_create_plan(request, project_id):
    ctx = build_context("Create Plan", action_url=request.path, extra={"project_id": project_id})

    if request.method == "POST":
        data = parse_request_data(request)
        payload = {
            "name": data.get("name", ""),
            "description": data.get("description", ""),
        }

        milestone_id = data.get("milestone_id")
        if milestone_id:
            payload["milestone_id"] = int(milestone_id)

        try:
            result = testrail_request("POST", f"add_plan/{project_id}", payload)
            ctx["success"] = "Plan créé avec succès."
            ctx["result"] = result
        except requests.HTTPError as e:
            handle_http_error(ctx, e)
        except Exception as e:
            ctx["error"] = str(e)

    return render(request, "testrail/plan_form.html", ctx)


def testrail_create_case(request, section_id):
    ctx = build_context("Create Case", action_url=request.path, extra={"section_id": section_id})

    if request.method == "POST":
        data = parse_request_data(request)
        payload = {
            "title": data.get("title", ""),
            "custom_steps_separated": [
                {
                    "content": data.get("steps", ""),
                    "expected": data.get("expected", ""),
                }
            ]
        }

        refs = data.get("refs")
        priority_id = data.get("priority_id")

        if refs:
            payload["refs"] = refs
        if priority_id:
            payload["priority_id"] = int(priority_id)

        try:
            result = testrail_request("POST", f"add_case/{section_id}", payload)
            ctx["success"] = "Case créée avec succès."
            ctx["result"] = result
        except requests.HTTPError as e:
            handle_http_error(ctx, e)
        except Exception as e:
            ctx["error"] = str(e)

    return render(request, "testrail/case_form.html", ctx)


def testrail_update_case(request, case_id):
    ctx = build_context("Update Case", action_url=request.path, extra={"case_id": case_id})

    if request.method == "POST":
        data = parse_request_data(request)
        payload = {}

        if data.get("title"):
            payload["title"] = data.get("title")
        if data.get("refs"):
            payload["refs"] = data.get("refs")
        if data.get("priority_id"):
            payload["priority_id"] = int(data.get("priority_id"))

        if data.get("steps") or data.get("expected"):
            payload["custom_steps_separated"] = [
                {
                    "content": data.get("steps", ""),
                    "expected": data.get("expected", ""),
                }
            ]

        try:
            result = testrail_request("POST", f"update_case/{case_id}", payload)
            ctx["success"] = "Case mise à jour avec succès."
            ctx["result"] = result
        except requests.HTTPError as e:
            handle_http_error(ctx, e)
        except Exception as e:
            ctx["error"] = str(e)

    return render(request, "testrail/case_update_form.html", ctx)


def testrail_statuses(request):
    ctx = build_context("TestRail Statuses")
    try:
        data = testrail_request("GET", "get_statuses")
        ctx["result"] = data
        ctx["statuses"] = data if isinstance(data, list) else data.get("statuses", [])
    except requests.HTTPError as e:
        handle_http_error(ctx, e)
    except Exception as e:
        ctx["error"] = str(e)
    return render(request, "testrail/statuses_list.html", ctx)


def testrail_close_run(request, run_id):
    ctx = build_context("Close Run", action_url=request.path, extra={"run_id": run_id})

    if request.method == "POST":
        try:
            result = testrail_request("POST", f"close_run/{run_id}", {})
            ctx["success"] = "Run fermé avec succès."
            ctx["result"] = result
        except requests.HTTPError as e:
            handle_http_error(ctx, e)
        except Exception as e:
            ctx["error"] = str(e)

    return render(request, "testrail/run_close_form.html", ctx)


def testrail_add_bulk_results(request, run_id):
    ctx = build_context("Add Bulk Results", action_url=request.path, extra={"run_id": run_id})

    if request.method == "POST":
        data = parse_request_data(request)
        results_text = data.get("results_json", "")

        try:
            results = json.loads(results_text) if isinstance(results_text, str) else data.get("results", [])
            payload = {"results": results}
            result = testrail_request("POST", f"add_results_for_cases/{run_id}", payload)
            ctx["success"] = "Résultats bulk ajoutés avec succès."
            ctx["result"] = result
        except requests.HTTPError as e:
            handle_http_error(ctx, e)
        except Exception as e:
            ctx["error"] = str(e)

    return render(request, "testrail/bulk_results_form.html", ctx)


def testrail_add_result(request, run_id, case_id):
    ctx = build_context("Add Result For Case", action_url=request.path, extra={"run_id": run_id, "case_id": case_id})

    if request.method == "POST":
        data = parse_request_data(request)
        payload = {
            "status_id": int(data.get("status_id")),
            "comment": data.get("comment", ""),
        }

        if data.get("version"):
            payload["version"] = data.get("version")
        if data.get("defects"):
            payload["defects"] = data.get("defects")
        if data.get("elapsed"):
            payload["elapsed"] = data.get("elapsed")

        try:
            result = testrail_request("POST", f"add_result_for_case/{run_id}/{case_id}", payload)
            ctx["success"] = "Résultat ajouté avec succès."
            ctx["result"] = result
        except requests.HTTPError as e:
            handle_http_error(ctx, e)
        except Exception as e:
            ctx["error"] = str(e)

    return render(request, "testrail/result_form.html", ctx)


def testrail_add_plan_entry(request, plan_id):
    ctx = build_context("Add Plan Entry", action_url=request.path, extra={"plan_id": plan_id})

    if request.method == "POST":
        data = parse_request_data(request)
        include_all = True if str(data.get("include_all", "true")).lower() in ["true", "1", "on", "yes"] else False

        payload = {
            "suite_id": int(data.get("suite_id")),
            "name": data.get("name", ""),
            "description": data.get("description", ""),
            "include_all": include_all,
        }

        milestone_id = data.get("milestone_id")
        case_ids = data.get("case_ids", "")

        if milestone_id:
            payload["milestone_id"] = int(milestone_id)

        if not include_all and case_ids:
            payload["case_ids"] = [int(x.strip()) for x in case_ids.split(",") if x.strip()]

        try:
            result = testrail_request("POST", f"add_plan_entry/{plan_id}", payload)
            ctx["success"] = "Plan entry ajoutée avec succès."
            ctx["result"] = result
        except requests.HTTPError as e:
            handle_http_error(ctx, e)
        except Exception as e:
            ctx["error"] = str(e)

    return render(request, "testrail/plan_entry_form.html", ctx)