import psycopg2

class Connection:

    def init(self):
        self.db=psycopg2.connect("dbname=Phones user=postgres password=1")

    def close(self):
        self.db.close()

    def selectAll(self, table):
        cur=self.db.cursor()
        cur.execute("SELECT * FROM public.\""+table+"\"")
        records=cur.fetchall()
        print(records)

    def fillBaseWithItems(self, modelName,items):
        cur=self.db.cursor()
        cur.execute("CREATE TABLE if not exists public.\""+modelName+"\"(id SERIAL NOT NULL,\"minPrice\" real,\"shopName\" character varying(150) COLLATE pg_catalog.\"default\",\"buyUrl\" character varying(600) COLLATE pg_catalog.\"default\",\"scrapDate\" date,\"maxPrice\" real)")
        self.insertToBd(modelName,items)
        self.db.commit()

    def insertToBd(self, modelName, items):
        cur=self.db.cursor()
        minPrice=0
        maxPrice=0
        for item in items:
            if len(item.prices)<2:
                minPrice=item.prices[0]
                maxPrice=item.prices[0]
            else:
                minPrice=item.prices[0]
                maxPrice=item.prices[1]

            cur.execute("INSERT INTO public.\""+modelName+"\"(\"minPrice\", \"shopName\", \"buyUrl\", \"scrapDate\", \"maxPrice\") VALUES ("+minPrice+",\'"+item.shopName+"\',\'"+item.url+"\',now()::date,"+maxPrice+");")