

install.packages("rpart")

install.packages("rpart.plot")

library(rpart)

library(rpart.plot)

data(iris)

model <- rpart(Species ~ Sepal.Length + Sepal.Width + Petal.Length + Petal.Width, data = iris, method = "class")

summary(model)

rpart.plot(model, extra = 1, main = "Decision Tree for Iris Dataset")

predictions <- predict(model, iris, type = "class")

table(predictions, iris$Species)

accuracy <- sum(predictions == iris$Species) / length(iris$Species)

cat("Accuracy: ", accuracy, "\n")
