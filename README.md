# Docs

1. Plate Detection Service

<div class="group relative my-4 rounded-lg"><pre class="scrollbar-custom overflow-auto px-5 scrollbar-thumb-gray-500 hover:scrollbar-thumb-gray-400 dark:scrollbar-thumb-white/10 dark:hover:scrollbar-thumb-white/20"><code class="language-bash">curl --location <span class="hljs-string">'http://{server_ip}:9394/detect'</span> --form <span class="hljs-string">'file_img=@"full.jpg"'</span>
		</code></pre> </div>


<ul>
<li><code>file_img</code>: The image file containing the vehicle license plate. The file should be sent as a multipart/form-data attachment.</li>
</ul>

Calling this API will return a json. Here is a sample json:

```json
{
    "result": {
        "plates": [
            {
                "box": {
                    "bottom": 387,
                    "left": 569,
                    "right": 761,
                    "top": 318
                },
                "legible": true,
                "ocr_accuracy": 0.7983546778559685,
                "plate_confidence": 0.9851707220077515,
                "plate_text": {
                    "city_code": "33",
                    "first_part": "25",
                    "letter": "ein",
                    "persian_letter": "ع",
                    "plate": "25ein12933",
                    "second_part": "129"
                },
                "plate_type": "iran"
            }
        ],
        "selected": null,
        "time": 0.14780855178833008
    },
    "success": true
}

```

Here is JSON Description:

<ul>
<li><code>result</code>: The result of the plate detection and recognition process.<ul>
<li><code>plates</code>: An array of detected plates. Each plate object contains the following properties:<ul>
<li><code>box</code>: The bounding box coordinates of the plate in the image.<ul>
<li><code>bottom</code>: The bottom coordinate of the plate.</li>
<li><code>left</code>: The left coordinate of the plate.</li>
<li><code>right</code>: The right coordinate of the plate.</li>
<li><code>top</code>: The top coordinate of the plate.</li>
</ul>
</li>
<li><code>legible</code>: A boolean indicating whether the plate is legible.</li>
<li><code>ocr_accuracy</code>: The accuracy of the OCR (Optical Character Recognition) process.</li>
<li><code>plate_confidence</code>: The confidence level of the plate detection and recognition process.</li>
<li><code>plate_text</code>: An object containing the extracted plate text.<ul>
<li><code>city_code</code>: The city code on the plate.</li>
<li><code>first_part</code>: The first part of the plate number.</li>
<li><code>letter</code>: The letter on the plate.</li>
<li><code>persian_letter</code>: The Persian letter on the plate (if applicable).</li>
<li><code>plate</code>: The full plate number.</li>
<li><code>second_part</code>: The second part of the plate number.</li>
</ul>
</li>
<li><code>plate_type</code>: The type of plate (e.g. "iran").</li>
</ul>
</li>
<li><code>selected</code>: Not used in this version of the API.</li>
<li><code>time</code>: The time taken to process the image.</li>
</ul>
</li>
<li><code>success</code>: A boolean indicating whether the request was successful.</li>
</ul>

Here is a complete list of Persian letters:

```json
plateLetters = [
    {"persian": "الف", "english": "alef", "value": 0},
    {"persian": "ب", "english": "b", "value": 1},
    {"persian": "ج", "english": "j", "value": 2},
    {"persian": "ل", "english": "l", "value": 3},
    {"persian": "م", "english": "m", "value": 4},
    {"persian": "ن", "english": "n", "value": 5},
    {"persian": "ق", "english": "q", "value": 6},
    {"persian": "و", "english": "v", "value": 7},
    {"persian": "ه", "english": "h", "value": 8},
    {"persian": "ی", "english": "y", "value": 9},
    {"persian": "د", "english": "d", "value": 10},
    {"persian": "س", "english": "s", "value": 11},
    {"persian": "ص", "english": "sad", "value": 12},
    {"persian": "معلول", "english": "malol", "value": 13},
    {"persian": "ت", "english": "t", "value": 14},
    {"persian": "ط", "english": "ta", "value": 15},
    {"persian": "ع", "english": "ein", "value": 16},
    {"persian": "D", "english": "diplomat", "value": 17},
    {"persian": "S", "english": "siyasi", "value": 18},
    {"persian": "پ", "english": "p", "value": 19},
    {"persian": "تشریفات", "english": "tashrifat", "value": 20},
    {"persian": "ث", "english": "the", "value": 21},
    {"persian": "ز", "english": "ze", "value": 22},
    {"persian": "ش", "english": "she", "value": 23},
    {"persian": "ف", "english": "fe", "value": 24},
    {"persian": "ک", "english": "kaf", "value": 25},
    {"persian": "گ", "english": "gaf", "value": 26},
    {"persian": "#", "english": "#", "value": 27}
]
```