# importing data
season <- read.csv("C:\\Users\\aethe\\OneDrive\\Desktop\\stats\\data for r.csv", stringsAsFactors = TRUE)
    View(season)

# logistic regression model
mylogit <- glm(Outcome ~ Warm.Up + Map + Score + Kills + Deaths + Assists,
               data = season,
               family = binomial)

# viewing the model
summary(mylogit)
# confint(mylogit)
    # confint() errors on this model
confint.default(mylogit)

# testing the model
new_data = data.frame(Warm.Up = "th",
                      Map = "Bank",
                      Score = 1420,
                      Kills = 5,
                      Deaths = 2,
                      Assists = 1)
predict(mylogit,
        new_data,
        "response")
# output:            1
#            0.6502007 
