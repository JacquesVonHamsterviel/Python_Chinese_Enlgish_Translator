def base64_translate(q):
  verify_key=str(random.randint(100000000,999999999))
  data={'text':base64.b64encode(q.encode()),'lan':'en','verify_key':verify_key}
  r=requests.post("http://127.0.0.1:5690/base64", data, headers=user_agent, timeout=60)
  print(r.content.decode('utf-8'))
  #time.sleep(1)
  if verify_key in base64.b64decode(r.content).decode():
    return(base64.b64decode(r.content).decode().replace('\n','')[len(verify_key):])
  else:
    raise Exception('API-DataError: '+str(base64.b64decode(r.content).decode().replace('\n','')))
    
 base64_translate("Example Text")
