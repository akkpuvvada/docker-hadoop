# Covid-19 bigdata project using Hadoop

## How to put data to hdfs

```bash
hdfs dfs -mkdir /user
hdfs dfs -mkdir /user/hduser
hdfs dfs -mkdir input
hdfs dfs -put {file_name} input
```

## Following information can be obtained from the project

- Number of cases registered as per age group

  ```bash
  hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar -mapper mapper.py -reducer reducer.py -input /user/hduser/input/main.csv -output /user/hduser/output22
  ```

- Number of deaths as per age group

  ```bash
  hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar -mapper dead_mapper.py -reducer dead_reducer.py -input /user/hduser/input/main.csv -output /user/hduser/output22
  ```

- Number of covid cases in different states

  ```bash
  hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar -mapper state_mapper.py -reducer state_reducer.py -input /user/hduser/input/main.csv -output /user/hduser/output22
  ```

- Number of deaths in each state

  ```bash
  hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar -mapper state_mapper.py -reducer state_dead_reducer.py -input /user/hduser/input/main.csv -output /user/hduser/output22
  ```
