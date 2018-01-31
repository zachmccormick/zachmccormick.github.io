import datetime
from pathlib import Path

from slugify import slugify


def new_post():
    # titles/slugs must be different per month
    title = input('Post title: ')
    slug = slugify(title)
    now = datetime.datetime.now()
    directory = 'content/{year}/{month}'.format(year=now.year, month=now.month)
    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)
    filename = path.joinpath('{slug}.md'.format(slug=slug))
    if filename.exists():
        print('File already exists: "{filename}"'.format(filename=filename))
        return

    # Get category, tags, etc.
    # TODO gather a list of categories or ML algo to auto-categorize
    # TODO algorithm to suggest tags post-article?
    category = input('Category: ')
    tags = []
    while True:
        tag = input('Tag:')
        if tag:
            tags.append(tag.strip())
        else:
            break
    with filename.open('w') as file:
        file.write('Title: {title}'.format(title=title))
        file.write('\n')
        file.write('Date: {date}'.format(date=now.isoformat()))
        file.write('\n')
        file.write('Category: {category}'.format(category=category))
        file.write('\n')
        file.write('Tags: {tags}'.format(tags=','.join(set(tags))))
        file.write('\n')
        file.write('Authors: Zach McCormick')
        file.write('\n')
        print('"vim {}"'.format(filename))


if __name__ == "__main__":
    new_post()
