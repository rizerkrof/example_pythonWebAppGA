from flask import Flask, render_template
import logging
app = Flask(__name__)

@app.route('/', methods=["GET"])
# def hello_world():
#     prefix_google = """
        # <!-- Google tag (gtag.js) -->
        # <script async src="https://www.googletagmanager.com/gtag/js?id=G-SSBHSGEKLF"></script>
        # <script>
        #     window.dataLayer = window.dataLayer || [];
        #     function gtag(){dataLayer.push(arguments);}
        #     gtag('js', new Date());
        #     gtag('config', 'G-SSBHSGEKLF');
        # </script>
#         <body>
#             <button onclick="func()">Click me</button>
#             <script src="googleAnalytics.js"></script>
#         </body>
#     """
#     return prefix_google + "Hello World"
def home():
    return render_template('home.html')

@app.route('/logger', methods=['GET'])
def logger():
    loggerLog = 'You entered logger page'
    app.logger.info(loggerLog)
    return render_template('logger.html', value=loggerLog)

if __name__ == '__main__':
    app.run(debug=True)
