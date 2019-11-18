# Preference -> Tools -> Python integrated Tools - Choose py.test as Default test runner.

import requests

date_name = ["Feb 16", "Mar 16", "Apr 16", "May 16", "Jun 16", "Jul 16", "Aug 16", "Sep 16", "Oct 16", "Nov 16", "Dec 16",
             "Jan 17","Feb 17", "Mar 17", "Apr 17", "May 17", "Jun 17", "Jul 17", "Aug 17", "Sep 17", "Oct 17", "Nov 17", "Dec 17",
             "Jan 18", "Feb 18"]

job_words = ["onsite", "on site", "remote", "position", "full-time", "full time", "Part Time"]
prog_language = ["Python", " C ", "C++", "Java ", "Swift", "JavaScript", " Go ", " R ", "C#", "Ruby"]

job_count =    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
onsite_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
remote_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
language_count = [0,0,0,0,0,0,0,0,0,0]


def download_json():
    object_id_list = []
    sample_query = 'https://hn.algolia.com/api/v1/search_by_date?query=Ask%20HN:%20Who%20is%20hiring%3F&tags=story&tags=author_whoishiring&numericFilters=created_at_i%3E1454284800,created_at_i%3C1519862400&hitsPerPage=30'
    web_response = requests.get(sample_query)
    json_data = web_response.json()
    for hit_data in json_data["hits"]:
        object_id_list.append(hit_data["objectID"])
    return object_id_list;


def read_all_comment(object_ids):
    month = 24
    for id in object_ids:
        sample_query = 'https://hn.algolia.com/api/v1/items/'
        sample_query += id
        web_response = requests.get(sample_query)
        json_data = web_response.json()
        for hit_data in json_data["children"]:
            text_comment = str(hit_data["text"])
            text_comment = text_comment.lower()
            for keyword in job_words:
                if keyword.lower() in text_comment:
                    job_count[month] += 1
                    break
            if "onsite" in text_comment:
                onsite_count[month] += 1
            if "remote" in text_comment:
                remote_count[month] += 1

            for i in range(0, len(prog_language)):
                if prog_language[i].lower() in text_comment:
                    language_count[i] += 1
                    continue

        print(date_name[month] + ": "+ id)
        month -= 1



if __name__ == "__main__":

    object_ids = download_json()
    read_all_comment(object_ids)
    print(job_count)



    print("Compete")
