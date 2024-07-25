def report_generator(title, author, date, /, *, summary="", conclusion=""):
    report = f"Title: {title}\n"
    report += f"Author: {author}\n"
    report += f"Date: {date}\n"

    if summary:
        report += f"Summary: {summary} \n"
    
    if conclusion:
        report += f"Conclusion: {conclusion}\n"
    
    return report

title = "Python Odyssey cours"
author = "Jane Brown"
date = "July 24, 2024"

print(report_generator(title, author, date, summary="This is a good course", conclusion="I'm recomending this course for you."))

