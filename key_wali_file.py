import os
import openai
from key_file import apikey

    openai.api_key = apikey

    prompt_in = "a"
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt_in,
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

print(response)
'''
{
  "warning": "This model version is deprecated. Migrate before January 4, 2024 to avoid disruption of service. Learn more https://platform.openai.com/docs/deprecations",
  "id": "cmpl-7u3Gz8cJCgt1JmPhuVwpfHBjOMFfO",
  "object": "text_completion",
  "created": 1693593305,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "package com.test.farza.miscatan.database;\n\nimport android.content.Context;\nimport android.database.sqlite.SQLiteDatabase;\nimport android.database.sqlite.SQLiteOpenHelper;\n\n/**\n * Created by farzaali on 5/14/16.\n */\npublic class DBHelper extends SQLiteOpenHelper {\n    public static final String DATABASE_NAME = \"MiscatanDb.db\";\n    public static final String DATABASE_TABLE = \"TABLE_CHART\";\n    public static final int DATABASE_VERSION = 1;\n\n    public static final String COL_ID = \"_id\";\n    public static final String COL_YEAR = \"year\";\n    public static final String COL_STATE = \"state\";\n    public static final String COL_VALUE = \"value\";\n\n    private static final String DATABASE_CREATE = \"create table \" + DATABASE_TABLE +\n            \" (\" + COL_ID + \" integer primary key autoincrement, \" +\n            COL_YEAR + \" integer not null, \" +\n            COL_STATE + \" text not null",
      "index": 0,
      "logprobs": null,
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 1,
    "completion_tokens": 256,
    "total_tokens": 257
  }
}
'''