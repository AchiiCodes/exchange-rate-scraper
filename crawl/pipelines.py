from sqlalchemy.orm import sessionmaker

from crawl.models import PottchangeItem, create_items_table, db_connect


class CrawlPipeline:
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates items table.
        """
        engine = db_connect()
        create_items_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        Process the item and store to database.
        """
        session = self.Session()
        instance = session.query(PottchangeItem).filter_by(**item).one_or_none()
        if instance:
            return instance
        rate_item = PottchangeItem(**item)

        try:
            session.add(rate_item)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
