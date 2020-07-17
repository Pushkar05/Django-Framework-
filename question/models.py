from django.db import models

# Here we create a class called Question. It has different fields
#We will migrate all these fields once the model is created
class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=200)
    c1 = models.CharField(max_length=200, default='')
    c2 = models.CharField(max_length=200, default='')
    c3 = models.CharField(max_length=200, default='')
    c4 = models.CharField(max_length=200, default='')
    answer = models.CharField(max_length=200, default='c1')
    marks = models.IntegerField(default=0)


    def __str__(self):
        return self.question_text

# We can include the name of the test in the test model
class Test(models.Model):

    test_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Association(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.test) + " ===> " + str(self.question)

    @classmethod
    def get_test_question_id(cls, test_id):
        association_obj = cls.objects.filter(test_id=test_id)
        question_id_list = [
            obj.question.question_id for obj in association_obj]
        return question_id_list



