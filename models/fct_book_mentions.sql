-- Step 3b: Flatten Book Mentions into Fact Table
SELECT
    VIDEO_ID,
    f.value::STRING AS BOOK_NAME,
    INSERTED_AT AS PROCESSED_AT
FROM {{ ref('stg_youtube_transcripts') }},
LATERAL FLATTEN(input => BOOK_NAMES_ARRAY) f
WHERE f.value IS NOT NULL