from python_framework import SqlAlchemyProxy as sap
from python_framework import Repository

from model import Investment


@Repository(model = Investment.Investment)
class InvestmentRepository:

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

    def findAllByQuery(self, query):
        return self.repository.findAllByQueryAndCommit(query, self.model)

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

    def findAllByKeyAndTypeIn(self, key, typeList):
        modelList = self.repository.session.query(self.model).filter(
            sap.and_(
                self.model.key == key,
                self.model.type.in_(typeList)
            )
        ).all()
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

    def findAllByQuery(self, query, additionalCondition=None):
        return self.repository.findAllByQueryAndCommit(query, self.model, additionalCondition=additionalCondition)

    def existsByQuery(self, query, additionalCondition=None):
        return self.repository.existsByQueryAndCommit(query, self.model, additionalCondition=additionalCondition)
