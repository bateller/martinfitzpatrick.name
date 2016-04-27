#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os
import json
import requests
import datetime
import argparse
import HTMLParser




parser = argparse.ArgumentParser()
parser.add_argument("min", help="Minimum Question scores to retrieve", type=int, default=5, nargs='?')
args = parser.parse_args()


h = HTMLParser.HTMLParser()


# Get all the answers
r = requests.get('https://api.stackexchange.com/2.2/users/754456/answers?pagesize=100&order=desc&sort=creation&site=stackoverflow&filter=!-*f(6t0UyTer')
answers = json.loads(r.content)

# Generate list of question IDs to get question metadata
filtered_answers = []
qids = []
for a in answers['items']:
    if a['score'] >= args.min: # Cut-off for 'general interest'
        filtered_answers.append(a)    
        qids.append( str(a['question_id']) )
    
r = requests.get('https://api.stackexchange.com/2.2/questions/%s?order=desc&sort=activity&site=stackoverflow' % ';'.join(qids))
questions = json.loads(r.content)

# Required metadata from the questions is link (basename), title, tags

metadata = {}

for q in questions['items']:
    metadata[q['question_id']] = {
        'question_link': q['link'],
        'slug': os.path.basename(q['link']),
        'title': q['title'],
        'tags': ','.join(q['tags']),
    }

# Now generate the outputs; for each answer

for a in filtered_answers:
    o = a.copy()
    o.update(metadata[a['question_id']])


    dt = datetime.datetime.fromtimestamp(o['creation_date'])
    o['date'] = dt.strftime('%Y-%m-%d %H:%M')
    fn = os.path.join(os.path.dirname(os.path.realpath(__file__)), o['slug'] + '.md')
    with open(fn, 'w') as f:
        s = u'''Date: {date}
Author: Martin Fitzpatrick
Email: martin.fitzpatrick@gmail.com
Title: {title}
Slug: {slug}
Tags: {tags}
Type: stackoverflow
Link: {share_link}/{user_id}
SO_question_url: {question_url}/{user_id}
SO_score: {score}
SO_accepted_answer: {is_accepted}
        
{body_markdown}
        '''.format(
            date=o['date'], 
            title=o['title'], 
            slug=o['slug'], 
            tags=o['tags'], 
            body_markdown=h.unescape(o['body_markdown']), 
            share_link=o['share_link'],
            question_url=o['question_link'],
            score=o['score'],
            is_accepted=o['is_accepted'],
            user_id=754456,
            )
        f.write(s.encode('utf8'))
    