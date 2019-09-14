import hashlib
import psycopg2
import psycopg2.extras
from flask import session
from app.app import app
from db.database_config import Database
from db.connection import start_connection, close_connection
from app.resources.Common.UsersCommon import UsersCommon

# from app.resources.Users.UserId import UserId


password = UsersCommon.to_hash('123Wertyq')
users = [
    {
        'email': "mr.andrey.sd@gmail.com",
        'login': 'Andrei',
        'password': password
    },
    {
        'email': "nik3.mr@gmail.com",
        'login': 'Artem',
        'password': password
    },
    {
        'email': "vladisslaww@gmail.com",
        'login': 'Vladislav',
        'password': password
    },
    {
        'email': "juliarychkova1@gmail.com",
        'login': 'Julia',
        'password': password
    },
    {
        'email': "curetoyou@gmail.com",
        'login': 'Vova',
        'password': password
    },
    {
        'email': "innmaster38@gmail.com",
        'login': 'Master',
        'password': password
    },
]

docs = ['ПАО НК Роснефть', 'ПАО РусГидро', 'ПАО Сбербанк']
votes = [
    'Мировой рынок: Если рассматривать мировой рынок, то в первую очередь стоит отметить то, что в странах СНГ и соседних странах с Россией схожая ситуация. Большие территории, одинаковая энергосистема и острая необходимость в улучшении работ по обслуживанию линий электропередачи. В Монголии же существует 6 ТЭЦ (за исключением ТЭЦ в Чойбалсане), которые соединены между собой двух цепными линиями 220 кВ. Кроме того Монгольская энергосистема тесно сотрудничает с АО «СО ЕЭС», протяженность линий компании составляет более 100 тысяч км.',
    'Дальнее зарубежье: В связи с тем, что наш проект заинтересовал транснациональной компанию schneider electric в рамках конкурса Go Green in the City, мы планируем через ее дочерние компании внедрить наше решение в страны Европы и Северной Америки, где основными потребителями с наибольшим объемом рынка и количеством повреждений',
    'Функциональные возможности «ЦРАП». Автоматическое ОМП в реальном времени — определение поврежденной линии, вида короткого замыкания и расстояния, учет взаимоиндукций линий и отпаек с выводом на индикатор всех возможных решений. ОМП производится с помощью метода по измерению реактанса и дистанционного (l-метода) (в ПК «QLines» реализованы те же функции, в подробном отчете представлены результаты расчета по методу измерения реактанса и дистанционного, а также расчет по более точному методу мгновенных значений);',
    'Характеристики В ПК «QLines» также реализован метод по определению места повреждения с помощью метода мгновенных значений, за счет того, что в данном ПК не требуется синхронизация по концам линий электропередач данный метод имеет преимущества в точности.',
    'Развитие инновационных технологий — еще одно важнейшее направление деятельности Компании. Так, в нефтепереработке началось применение катализаторов собственного производства для риформинга и водородных установок. На всех установках каталитического крекинга осуществлен переход на использование только отечественных катализаторов.',
    'В своей деятельности ОАО «НК «Роснефть», являясь публичной компаний с государственным участием, придерживается самых высоких стандартов в области корпоративного управления, соблюдая принципы и рекомендации Кодекса корпоративного управления Банка России, что обеспечивает долгосрочное и устойчивое развитие Компании, защиту интересов ее акционеров и инвесторов.',
    'Особо подчеркну, что, наряду со значительными достижениями в области производства углеводородов, ОАО «НК «Роснефть» демонстрирует значимые результаты в части замещения запасов, в течение более десяти лет этот коэффициент значительно превышает 100 %.',
    'ОАО «НК «РОСНЕФТЬ» ЯВЛЯЕТСЯ ЛИДЕРОМ РОССИЙСКОЙ НЕФТЯНОЙ ОТРАСЛИ И КРУПНЕЙШЕЙ В МИРЕ ПУБЛИЧНОЙ НЕФТЯНОЙ КОМПАНИЕЙ ПО ОБЪЕМУ ЗАПАСОВ И ДОБЫЧИ.',
    'Если Договором, условиями которого установлен Неснижаемый остаток, предусмотрена возможность увеличения процентной ставки в течение первоначального/пролонгированного срока Договора, то её увеличение производится при условии установления Вкладчиком нового, более высокого Неснижаемого остатка.',
    'Операции по Счету вклада выполняются в соответствии с законодательством Российской Федерации по предъявлении Вкладчиком, Представителем или Вносителем паспорта или иного документа, удостоверяющего личность.',
    'Нарушение условий Вклада в результате списания денежных средств со Счета вклада на основании решения суда или в иных случаях, предусмотренных законодательством.',
    'Дополнительные взносы могут быть внесены в наличном или безналичном порядке с даты списания денежных средств до даты окончания первоначального/пролонгированного срока, в котором произведено списание;'
]
chats = ['Опрос 1', 'Опрос 2', 'Опрос 3', 'Опрос 4', 'Опрос 1', 'Опрос 2', 'Опрос 3', 'Опрос 4', 'Опрос 1', 'Опрос 2', 'Опрос 3', 'Опрос 4']

def create_docs_votes(doc_id):
    for vote_id in range(1, 5):
        sql = """   INSERT INTO  docs_votes (vote_id, doc_id)
                    VALUES (%s, %s)
                    ;"""
        record = (vote_id, doc_id)
        cursor.execute(sql, record)
        connection.commit()


def create_vote(vote):
    sql = """INSERT INTO   votes (vote_text)
                     VALUES (%s)
                    ;"""
    record = (vote,)
    cursor.execute(sql, record)
    connection.commit()

def create_chats(chat, vote_id, docid):
    sql = """INSERT INTO   chats (chat_name, vote_id, doc_id)
                     VALUES (%s, %s, %s)
                    ;"""
    record = (chat,vote_id, docid)
    cursor.execute(sql, record)
    connection.commit()


def create_user(user):
    sql = """INSERT INTO   users (email, login, password)
                     VALUES (%s, %s, %s)
                    ;"""
    record = (user['email'], user['login'], user['password'])
    cursor.execute(sql, record)
    connection.commit()

def create_doc(doc):
    sql = """   INSERT INTO   docs (doc_name)
                VALUES (%s)
            ;"""
    record = (doc,)
    cursor.execute(sql, record)
    connection.commit()


def create_docs_users(doc_id, user_for_docs):
    for user_id in range(1, user_for_docs):
        sql = """   INSERT INTO  docs_users (user_id, doc_id)
                    VALUES (%s, %s)
                    ;"""
        record = (user_id, doc_id)
        cursor.execute(sql, record)
        connection.commit()

connection, cursor = start_connection()
try:
    for doc in docs:
        create_doc(doc)
    for user in users:
        create_user(user)
    #docs_users
    for doc_id in range(1, len(docs) + 1):
        if doc_id == 1:
            user_for_docs = len(users) + 1
        elif doc_id == 2:
            user_for_docs = len(users)
        else:
            user_for_docs = len(users) - 1
        create_docs_users(doc_id, user_for_docs)
#     votes
    for vote in votes:
        create_vote(vote)
    i = 0
    docid = 1
    # chats
    for chat in chats:
        i += 1
        create_chats(chat, i, docid)
        if i % 4 == 0:
            docid += 1
#     docs_votes
    for doc_id in range(1, len(docs) + 1):
        create_docs_votes(doc_id)

except Exception as e:
    print(e)
finally:
    close_connection(connection, cursor)
