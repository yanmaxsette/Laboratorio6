#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sprint1.py
#  
#  Copyright 2020 Yan <yan@yan-Inspiron-5558>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import requests
import json

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'bearer #################################',
}

data = '{"query": "{ search(query:\\"stars:>100\\", type:REPOSITORY, first:100){ nodes { ... on Repository {nameWithOwner url createdAt updatedAt pullRequests{ totalCount } releases{ totalCount } primaryLanguage{ name } all_issues: issues{ totalCount } closed_issues: issues(states:CLOSED){ totalCount } } } } }"}'

response = requests.post('https://api.github.com/graphql', headers=headers, data=data)

if response.status_code != 200:
	print ("ERRO - cheque o codigo")
	
json_data = json.loads(response.text)

#resposta da consulta:
print(json_data)

#proximas entregas:

'''
nodes = json_data['data']['search']['nodes']

url=[]
nameWithOwner=[]
pullRequests=[]
primaryLanguage=[]
releases=[]
issues=[]
updatedAt=[]
createdAt=[]

for repos in nodes:
	createdAt.append(repos['createdAt'])
	pullRequests.append(repos['pullRequests']['totalCount'])
	releases.append(repos['releases']['totalCount'])
	updatedAt.append(repos['updatedAt'])
	if repos['primaryLanguage'] is None:
		primaryLanguage.append("Nao informado")
	else:
		primaryLanguage.append(repos['primaryLanguage']['name'])
	if repos['all_issues']['totalCount'] == 0:
		issues.append("Nao possui issue")
	else:
		issues.append(repos['closed_issues']['totalCount']/repos['all_issues']['totalCount'])

print("RQ 01. Sistemas populares são maduros/antigos?")    
print (createdAt)

print("")

print("RQ 02. Sistemas populares recebem muita contribuição externa?")       
print (pullRequests)

print("")

print("RQ 03. Sistemas populares lançam releases com frequência?")   
print (releases)

print("")

print("RQ 04. Sistemas populares são atualizados com frequência?")   
print (updatedAt)

print("")

print("RQ 05. Sistemas populares são escritos nas linguagens mais populares?") 
print (primaryLanguage)

print("")
  
print("RQ 06. Sistemas populares possuem um alto percentual de issues fechadas?")   
print (issues)

print("")

print("[BONUS] RQ. 07: Sistemas escritos em linguagens mais populares recebem mais contribuição externa, lançam mais releases e são atualizados com mais frequência?")   
'''
