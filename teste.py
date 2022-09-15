from redis import Redis
import json
r = Redis(password="Quartz00")
r.hset("teste_variables","ipva_relatorio",json.dumps({}))
print(json.loads(r.hget("teste_variables","ipva_relatorio")))
r.delete("teste_variables")
r.hset("teste_variables","ipva_relatorio",json.dumps({}))
print(json.loads(r.hget("teste_variables","ipva_relatorio")))
#print(json.loads(r.hget("teste_variables","ipva_relatorio")))
r.rpush("teste:hash:variables:key","1")
print(r.lindex("teste:hash:variables:key",1))
#print(r.blpop("teste:hash:variables:key",5))
r.sadd("teste","teste")
r.sadd("teste","teste1")
print(r.smembers("teste"))