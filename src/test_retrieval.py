from retrieval import *
#from faq_loader import standardize_faq_keys

import os
import json 

# Example FAQs


base_dir = os.path.dirname(os.path.abspath(__file__))
faq_path = os.path.join(base_dir, "..", "data", "faq.json")
with open(faq_path, "r", encoding="utf-8") as f:
    faq_texts = json.load(f)



#faq_path = "../faq-floripa/data/faq.json"



#faq_texts = [
#  {
#    "id": "faq001",
#    "question_pt": "Onde fica Florianópolis?",
#    "answer_pt": "Florianópolis é a capital do estado de Santa Catarina, no sul do Brasil.",
#    "question_en": "Where is Florianópolis located?",
#    "answer_en": "Florianópolis is the capital of the state of Santa Catarina, in southern Brazil."
#  },
#  {
#    "id": "faq002",
#    "question_pt": "Qual é a língua oficial falada em Florianópolis?",
#    "answer_pt": "A língua oficial é o português.",
#    "question_en": "What is the official language spoken in Florianópolis?",
#    "answer_en": "The official language is Portuguese."
#  },
#  {
#    "id": "faq003",
#    "question_pt": "Quais são as praias mais famosas da cidade?",
#    "answer_pt": "Praias como Joaquina, Campeche e Jurerê Internacional são muito populares.",
#    "question_en": "What are the most famous beaches in the city?",
#    "answer_en": "Beaches like Joaquina, Campeche, and Jurerê Internacional are very popular."
#  },
#  {
#    "id": "faq004",
#    "question_pt": "Qual a melhor época para visitar Florianópolis?",
#    "answer_pt": "A melhor época é durante o verão, de dezembro a março.",
#    "question_en": "What is the best time to visit Florianópolis?",
#    "answer_en": "The best time is during summer, from December to March."
#  },
#  {
#    "id": "faq005",
#    "question_pt": "Como é o clima na cidade?",
#    "answer_pt": "O clima é subtropical, com verões quentes e invernos amenos.",
#    "question_en": "How is the climate in the city?",
#    "answer_en": "The climate is subtropical, with hot summers and mild winters."
#  },
#  {
#    "id": "faq006",
#    "question_pt": "Floripa é uma cidade segura para turistas?",
#    "answer_pt": "Sim, é relativamente segura, mas sempre é recomendável tomar cuidado com pertences pessoais.",
#    "question_en": "Is Floripa a safe city for tourists?",
#    "answer_en": "Yes, it is relatively safe, but it is always recommended to be careful with personal belongings."
#  },
#  {
#    "id": "faq007",
#    "question_pt": "Quais são as opções de transporte público?",
#    "answer_pt": "Há linhas de ônibus que cobrem a ilha, além de táxis e aplicativos de transporte.",
#    "question_en": "What public transport options are available?",
#    "answer_en": "There are bus lines covering the island, as well as taxis and ride-hailing apps."
#  },
#  {
#    "id": "faq008",
#    "question_pt": "Existem opções de turismo ecológico?",
#    "answer_pt": "Sim, há trilhas, parques e reservas naturais para visitar.",
#    "question_en": "Are there ecotourism options?",
#    "answer_en": "Yes, there are trails, parks, and nature reserves to visit."
#  },
#  {
#    "id": "faq009",
#    "question_pt": "Onde posso provar a culinária local?",
#    "answer_pt": "Restaurantes no centro e próximos às praias servem pratos típicos como frutos do mar.",
#    "question_en": "Where can I try local cuisine?",
#    "answer_en": "Restaurants downtown and near the beaches serve typical dishes such as seafood."
#  },
#  {
#    "id": "faq010",
#    "question_pt": "Quais eventos culturais acontecem na cidade?",
#    "answer_pt": "Eventos como o Festival de Dança e a Marejada são bem conhecidos.",
#    "question_en": "What cultural events happen in the city?",
#    "answer_en": "Events like the Dance Festival and Marejada are well-known."
#  },
#  {
#    "id": "faq011",
#    "question_pt": "Como é o custo de vida em Florianópolis?",
#    "answer_pt": "O custo é moderado, mas pode ser alto em áreas turísticas no verão.",
#    "question_en": "How is the cost of living in Florianópolis?",
#    "answer_en": "The cost is moderate, but can be high in tourist areas during summer."
#  },
#  {
#    "id": "faq012",
#    "question_pt": "Posso usar dólar em Florianópolis?",
#    "answer_pt": "A moeda oficial é o real, mas alguns lugares aceitam dólar ou cartão internacional.",
#    "question_en": "Can I use dollars in Florianópolis?",
#    "answer_en": "The official currency is the real, but some places accept dollars or international cards."
#  },
#  {
#    "id": "faq013",
#    "question_pt": "Como funciona o sistema de saúde na cidade?",
#    "answer_pt": "Há hospitais públicos e privados, com bom atendimento na maioria das áreas.",
#    "question_en": "How does the healthcare system work in the city?",
#    "answer_en": "There are public and private hospitals, with good care in most areas."
#  },
#  {
#    "id": "faq014",
#    "question_pt": "É fácil encontrar internet e Wi-Fi?",
#    "answer_pt": "Sim, a maioria dos hotéis, cafés e locais públicos oferecem Wi-Fi.",
#    "question_en": "Is it easy to find internet and Wi-Fi?",
#    "answer_en": "Yes, most hotels, cafés, and public places offer Wi-Fi."
#  },
#  {
#    "id": "faq015",
#    "question_pt": "Quais são as melhores atividades ao ar livre?",
#    "answer_pt": "Surf, trilhas, passeio de barco e ciclismo são muito populares.",
#    "question_en": "What are the best outdoor activities?",
#    "answer_en": "Surfing, hiking, boat tours, and cycling are very popular."
#  },
#  {
#    "id": "faq016",
#    "question_pt": "Onde posso alugar bicicletas ou pranchas de surf?",
#    "answer_pt": "Lojas perto das praias oferecem aluguel de equipamentos esportivos.",
#    "question_en": "Where can I rent bikes or surfboards?",
#    "answer_en": "Shops near the beaches offer sports equipment rentals."
#  },
#  {
#    "id": "faq017",
#    "question_pt": "Quais bairros são bons para hospedagem?",
#    "answer_pt": "Lagoa da Conceição, Centro e Jurerê são opções populares.",
#    "question_en": "Which neighborhoods are good for accommodation?",
#    "answer_en": "Lagoa da Conceição, downtown, and Jurerê are popular options."
#  },
#  {
#    "id": "faq018",
#    "question_pt": "Como é a vida noturna em Florianópolis?",
#    "answer_pt": "Bares e clubes principalmente na Lagoa da Conceição são bastante animados.",
#    "question_en": "How is the nightlife in Florianópolis?",
#    "answer_en": "Bars and clubs especially in Lagoa da Conceição are very lively."
#  },
#  {
#    "id": "faq019",
#    "question_pt": "Existem aeroportos na cidade?",
#    "answer_pt": "Sim, o Aeroporto Hercílio Luz atende voos nacionais e alguns internacionais.",
#    "question_en": "Are there airports in the city?",
#    "answer_en": "Yes, Hercílio Luz Airport serves domestic and some international flights."
#  },
#  {
#    "id": "faq020",
#    "question_pt": "Como me deslocar do aeroporto para o centro?",
#    "answer_pt": "Táxis, ônibus e aplicativos de transporte são disponíveis na saída do aeroporto.",
#    "question_en": "How do I get from the airport to downtown?",
#    "answer_en": "Taxis, buses, and ride-sharing apps are available at the airport exit."
#  },
#  {
#    "id": "faq021",
#    "question_pt": "Quais são os pontos turísticos imperdíveis?",
#    "answer_pt": "Ponte Hercílio Luz, Praia Mole e o centro histórico são visitas obrigatórias.",
#    "question_en": "What are must-see tourist spots?",
#    "answer_en": "Hercílio Luz Bridge, Praia Mole, and the historic downtown are must-visits."
#  },
#  {
#    "id": "faq022",
#    "question_pt": "Florianópolis é acessível para pessoas com mobilidade reduzida?",
#    "answer_pt": "Algumas áreas possuem acessibilidade, mas nem todas as praias têm infraestrutura adequada.",
#    "question_en": "Is Florianópolis accessible for people with reduced mobility?",
#    "answer_en": "Some areas have accessibility, but not all beaches have adequate infrastructure."
#  },
#  {
#    "id": "faq023",
#    "question_pt": "Onde posso comprar artesanato local?",
#    "answer_pt": "Feiras de artesanato no centro e nas praias oferecem produtos típicos.",
#    "question_en": "Where can I buy local crafts?",
#    "answer_en": "Craft fairs downtown and on the beaches offer typical products."
#  },
#  {
#    "id": "faq024",
#    "question_pt": "Existem opções vegetarianas na cidade?",
#    "answer_pt": "Sim, muitos restaurantes oferecem pratos vegetarianos e veganos.",
#    "question_en": "Are there vegetarian options in the city?",
#    "answer_en": "Yes, many restaurants offer vegetarian and vegan dishes."
#  },
#  {
#    "id": "faq025",
#    "question_pt": "Quais os cuidados com o meio ambiente na ilha?",
#    "answer_pt": "Há campanhas de preservação e áreas de proteção ambiental importantes.",
#    "question_en": "What environmental care measures exist on the island?",
#    "answer_en": "There are preservation campaigns and important protected environmental areas."
#  },
#  {
#    "id": "faq026",
#    "question_pt": "Qual a melhor forma de se locomover pela ilha?",
#    "answer_pt": "Alugar um carro é ideal para explorar melhor as praias e trilhas.",
#    "question_en": "What is the best way to get around the island?",
#    "answer_en": "Renting a car is ideal to better explore beaches and trails."
#  },
#  {
#    "id": "faq027",
#    "question_pt": "Existem hospitais de emergência na ilha?",
#    "answer_pt": "Sim, há hospitais públicos e privados com pronto atendimento.",
#    "question_en": "Are there emergency hospitals on the island?",
#    "answer_en": "Yes, there are public and private hospitals with emergency care."
#  },
#  {
#    "id": "faq028",
#    "question_pt": "Posso usar cartão de crédito para pagar na maioria dos lugares?",
#    "answer_pt": "Sim, cartões de crédito são amplamente aceitos.",
#    "question_en": "Can I use credit cards to pay in most places?",
#    "answer_en": "Yes, credit cards are widely accepted."
#  },
#  {
#    "id": "faq029",
#    "question_pt": "Existem museus para visitar na cidade?",
#    "answer_pt": "Sim, o Museu Histórico e o Museu do Mar são algumas opções.",
#    "question_en": "Are there museums to visit in the city?",
#    "answer_en": "Yes, the Historical Museum and the Sea Museum are some options."
#  },
#  {
#    "id": "faq030",
#    "question_pt": "Floripa é boa para prática de esportes ao ar livre?",
#    "answer_pt": "Sim, esportes como surf, kitesurf e trilhas são muito populares.",
#    "question_en": "Is Floripa good for outdoor sports?",
#    "answer_en": "Yes, sports like surfing, kitesurfing, and hiking are very popular."
#  },
#  {
#    "id": "faq031",
#    "question_pt": "Quais são as melhores praias para famílias com crianças?",
#    "answer_pt": "Praias como Jurerê Internacional e Daniela são calmas e indicadas para crianças.",
#    "question_en": "What are the best beaches for families with children?",
#    "answer_en": "Beaches like Jurerê Internacional and Daniela are calm and kid-friendly."
#  },
#  {
#    "id": "faq032",
#    "question_pt": "Qual é a melhor época para visitar Florianópolis?",
#    "answer_pt": "Entre novembro e março, quando o clima está mais quente e ideal para praia.",
#    "question_en": "What is the best time to visit Florianópolis?",
#    "answer_en": "Between November and March, when the weather is warmer and ideal for the beach."
#  },
#  {
#    "id": "faq033",
#    "question_pt": "Existem festivais culturais durante o ano?",
#    "answer_pt": "Sim, como o Festival de Dança e a Marejada, festa típica da região.",
#    "question_en": "Are there cultural festivals throughout the year?",
#    "answer_en": "Yes, like the Dance Festival and Marejada, a typical regional festivity."
#  },
#  {
#    "id": "faq034",
#    "question_pt": "Como é a segurança em Florianópolis?",
#    "answer_pt": "A cidade é relativamente segura, mas é sempre bom tomar cuidados básicos.",
#    "question_en": "How is the safety in Florianópolis?",
#    "answer_en": "The city is relatively safe, but it’s always good to take basic precautions."
#  },
#  {
#    "id": "faq035",
#    "question_pt": "Quais esportes aquáticos posso praticar?",
#    "answer_pt": "Surf, kitesurf, windsurf e stand-up paddle são muito populares.",
#    "question_en": "What water sports can I practice?",
#    "answer_en": "Surfing, kitesurfing, windsurfing, and stand-up paddleboarding are very popular."
#  },
#  {
#    "id": "faq036",
#    "question_pt": "Existem bons hotéis perto das praias?",
#    "answer_pt": "Sim, várias opções de hotéis e pousadas ficam próximos das praias principais.",
#    "question_en": "Are there good hotels near the beaches?",
#    "answer_en": "Yes, many hotels and inns are located near the main beaches."
#  },
#{
#    "id": "faq037",
#    "question_pt": "A ilha é boa para quem gosta de vida noturna?",
#    "answer_pt": "Sim, bairros como Lagoa da Conceição têm bares e baladas animadas.",
#    "question_en": "Is the island good for those who enjoy nightlife?",
#    "answer_en": "Yes, neighborhoods like Lagoa da Conceição have lively bars and clubs."
#  },
#  {
#    "id": "faq038",
#    "question_pt": "Posso levar meu pet para a praia?",
#    "answer_pt": "Algumas praias aceitam pets, mas é bom verificar regras locais antes.",
#    "question_en": "Can I bring my pet to the beach?",
#    "answer_en": "Some beaches allow pets, but it’s good to check local rules beforehand."
#  },
#  {
#    "id": "faq039",
#    "question_pt": "Como funcionam os meios de transporte na ilha?",
#    "answer_pt": "Há ônibus urbanos, táxis e apps de transporte como Uber e 99.",
#    "question_en": "How does transportation work on the island?",
#    "answer_en": "There are urban buses, taxis, and ride-sharing apps like Uber and 99."
#  },
#  {
#    "id": "faq040",
#    "question_pt": "Quais são os pratos típicos que devo experimentar?",
#    "answer_pt": "Sequência de camarão, ostras frescas e peixe assado são imperdíveis.",
#    "question_en": "What typical dishes should I try?",
#    "answer_en": "Shrimp sequence, fresh oysters, and baked fish are must-tries."
#  },
#  {
#    "id": "faq041",
#    "question_pt": "É fácil encontrar supermercados na ilha?",
#    "answer_pt": "Sim, há supermercados e mercados locais espalhados pela cidade.",
#    "question_en": "Is it easy to find supermarkets on the island?",
#    "answer_en": "Yes, there are supermarkets and local markets throughout the city."
#  },
#  {
#    "id": "faq042",
#    "question_pt": "Floripa é uma cidade cara para se viver?",
#    "answer_pt": "Comparada a outras capitais brasileiras, o custo de vida é moderado.",
#    "question_en": "Is Floripa an expensive city to live in?",
#    "answer_en": "Compared to other Brazilian capitals, the cost of living is moderate."
#  },
#  {
#    "id": "faq043",
#    "question_pt": "Quais são as opções de lazer para crianças?",
#    "answer_pt": "Parques, aquários e praias calmas são ótimas opções para crianças.",
#    "question_en": "What are the leisure options for children?",
#    "answer_en": "Parks, aquariums, and calm beaches are great options for kids."
#  },
#  {
#    "id": "faq044",
#    "question_pt": "Há eventos esportivos locais?",
#    "answer_pt": "Sim, corridas, campeonatos de surf e torneios de futebol acontecem frequentemente.",
#    "question_en": "Are there local sports events?",
#    "answer_en": "Yes, races, surfing championships, and soccer tournaments happen frequently."
#  },
#  {
#    "id": "faq045",
#    "question_pt": "Como é o transporte público para as praias mais distantes?",
#    "answer_pt": "Nem todas as praias têm acesso fácil por ônibus, alguns lugares exigem carro.",
#    "question_en": "How is public transport to the more distant beaches?",
#    "answer_en": "Not all beaches have easy bus access; some places require a car."
#  },
#  {
#    "id": "faq046",
#    "question_pt": "Quais tipos de lixo são coletados separadamente?",
#    "answer_pt": "Os principais tipos coletados separadamente são lixo comum, recicláveis (papel, plástico, vidro, metal) e lixo orgânico.",
#    "question_en": "What types of waste are collected separately?",
#    "answer_en": "The main types collected separately are regular waste, recyclables (paper, plastic, glass, metal), and organic waste."
#  },
#  {
#    "id": "faq047",
#    "question_pt": "Onde devo descartar resíduos perigosos ou eletrônicos?",
#    "answer_pt": "Resíduos perigosos e eletrônicos devem ser levados a pontos de coleta específicos indicados pela prefeitura.",
#    "question_en": "Where should I dispose of hazardous or electronic waste?",
#    "answer_en": "Hazardous and electronic waste must be taken to specific collection points designated by the city hall."
#  },
#  {
#    "id": "faq048",
#    "question_pt": "Como posso saber o dia da coleta no meu bairro?",
#    "answer_pt": "Você pode consultar o calendário de coleta no site da prefeitura ou ligar para o serviço de atendimento ao cidadão.",
#    "question_en": "How can I find out the garbage collection day in my neighborhood?",
#    "answer_en": "You can check the collection schedule on the city hall’s website or call the citizen service."
#  },
#  {
#    "id": "faq049",
#    "question_pt": "Florianópolis oferece serviço de coleta seletiva?",
#    "answer_pt": "Sim, a coleta seletiva é um programa oficial que visa incentivar a separação do lixo para reciclagem.",
#    "question_en": "Does Florianópolis offer selective waste collection service?",
#    "answer_en": "Yes, selective collection is an official program aimed at encouraging waste separation for recycling."
#  }
#
#
#]
#

#retriever = FAQRetrieverTFIDF(faq_texts)

#retriever = FAQRetrieverEmbedder(faq_texts)
#
#def main():
#    print("Ask a question (type 'exit' to quit):")
#    while True:
#        question = input("> ")
#        if question.lower() == "exit":
#            break
#        results = retriever.retrieve(question)
#        if not results:
#            print("No FAQ found matching your question.\n")
#            continue
#        best_match, score = results[0]
#        print(f"Best match: '{best_match}' (score: {score:.3f})\n")



#retriever = FAQRetrieverEmbedder(faq_texts)
#
#def main():
#    print("Ask a question (type 'exit' to quit):")
#    while True:
#        question = input("> ")
#        if question.lower().strip() == "exit":
#            break
#        if not question.strip():
#            print("Please enter a valid question.\n")
#            continue
#
#        results = retriever.retrieve(question)
#        if not results:
#            print("No FAQ found matching your question.\n")
#            continue
#
#        best_match, score = results[0]
#        print(f"Best match: '{best_match}' (score: {score:.3f})\n")
#
#if __name__ == "__main__":
#    main()




#retriever_pt = MultilingualFAQRetrieverEmbedder(faq_texts, language='pt')
retriever = FAQRetriever(faq_texts,language = None)
retriever_tf =  FAQRetrieverTFIDF(faq_texts,language = None)  #-> Aceita None 

query = "What kinds of trash are collected in separate bins?"

print("🔎 Pergunta:", query)
results = retriever.retrieve(query) #, language = None) #language = 'en')  #,language= None)
if results:

    for result in results:
        print(f"✅ Resposta: {result['answer']} (score: {result['score']:.3f})\n")



