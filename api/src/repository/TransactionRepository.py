from python_helper import ObjectHelper
from python_framework import SqlAlchemyProxy as sap
from python_framework import Repository

from model import Transaction


@Repository(model = Transaction.Transaction)
class TransactionRepository:

    def save(self, model):
        return self.repository.saveAndCommit(model)

    def saveAll(self, modelList):
        return self.repository.saveAllAndCommit(modelList)

    def findAll(self):
        return self.repository.findAllAndCommit(self.model)

    def findByKey(self, key):
        return self.repository.findByKeyAndCommit(key, self.model)

    def findAllByKeyIn(self, keyList):
        return self.repository.findAllByKeyInAndCommit(keyList)

    def existsByKey(self, key):
        return self.repository.existsByKeyAndCommit(key, self.model)

    def notExistsByKey(self, key):
        return not self.existsByKey(key)

    def deleteByKey(self, key):
        self.repository.deleteByKeyAndCommit(key, self.model)

    def findById(self, id):
        return self.repository.findByIdAndCommit(id, self.model)

    def findAllByIdIn(self, idList):
        return self.repository.findAllByIdInAndCommit(idList)

    def existsById(self, id):
        return self.repository.existsByIdAndCommit(id, self.model)

    def notExistsById(self, id):
        return not self.existsById(id)

    def deleteById(self, id):
        self.repository.deleteByIdAndCommit(id, self.model)

    def findAllByTypeIn(self, typeList):
        modelList = self.repository.session.query(self.model).filter(self.model.type.in_(typeList)).all()
        self.repository.session.commit()
        return self.repository.load(modelList)

    def findAllByKeyInAndTypeIn(self, keyList, typeList):
        modelList = self.repository.session.query(self.model).filter(
            sap.and_(
                self.model.key.in_(keyList),
                self.model.type.in_(typeList)
            )
        ).all()
        self.repository.session.commit()
        return self.repository.load(modelList)

    def findAllByQuery(self, query, fromDateTime, toDateTime):
        modelList = self.repository.session.query(self.model).filter(
            sap.and_(
                self.model.transactionAt >= fromDateTime,
                self.model.transactionAt <= toDateTime
            )
        ).filter_by(
            **{
                k: v
                for k, v in query.items()
                if ObjectHelper.isNotNone(v)
            }
        ).all()
        self.repository.session.commit()
        return self.repository.load(modelList)

    def findAllByOperationKeyIn(self, operationKeyList):
        modelList = self.repository.session.query(self.model).filter(self.model.operationKey.in_(operationKeyList)).all()
        self.repository.session.commit()
        return self.repository.load(modelList)
