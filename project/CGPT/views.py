from django.shortcuts import render 
from django.http import JsonResponse 
from django.conf import settings
import openai
import os
from .PROMPT_AI import *

API_KEY = settings.API_KEY
# # openai.api_key='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' #앞서 자신이 부여받은 API key를 넣으면 된다. 절대 외부에 공개해서는 안된다.
client = openai.OpenAI(api_key = API_KEY)
def get_completion(prompt): 
	print(prompt)
	query = client.chat.completions.create( 
		model="gpt-3.5-turbo",
		messages=[
            {
                'role':'system',
                'content': PROMPT_TEXT_SYSTEM
            },
            {
                'role':'user',
                'content': PROMPT_TEXT_USER_PLACE
            },
            {
                'role':'assistant',
                'content': PROMPT_TEXT_ASSISTANT_PLACE
            },
            {
                'role':'user',
                'content': PROMPT_TEXT_USER_QUERY
            },
            {
                'role':'user',
                'content': PROMPT_TEXT_USER_EXAMPLE_Q
            },
            {
                'role':'assistant',
                'content': PROMPT_TEXT_ASSISTANT_JSON
            },
        	{
                'role':'user',
                'content': prompt
            }
    	], 
		max_tokens=1024, 
		n=1, 
		stop=None, 
		temperature=0.5,
	) 
	response = query.choices[0].message.content
	print(response)
	return response 


def query_view(request): 
	if request.method == 'POST': 
		prompt = request.POST.get('prompt') 
		prompt=str(prompt)
		response = get_completion(prompt)
		return JsonResponse({'response': response}) 
	return render(request, 'index.html') 
