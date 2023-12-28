import json
import requests


def get_page_trud(page=0):
    """Gets a page of vacancies from the HeadHunter API.

    Args:
      page: The page number.

    Returns:
      A JSON object containing the vacancies.
    """

    params = {
        "offset": page,
        #         'limit': 100
    }

    req = requests.get("https://russia.superjob.ru/jsapi3/0.1/vacancy/", params)

    data = req.content.decode()
    req.close()

    return data


trud_jobs_objs = []

for page in range(0, 2):
    jobs_obj = json.loads(get_page_trud(page))
    trud_jobs_objs.append(jobs_obj)
#   print(jobs_obj)


#   time.sleep(0.25)

print("finished the search")
len(trud_jobs_objs)
