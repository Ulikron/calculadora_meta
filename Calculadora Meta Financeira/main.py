from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
  meta = float(request.form['meta'])
  economia_mensal = float(request.form['economia_mensal'])
  tempo_necessario = calcular_tempo_para_meta(meta, economia_mensal)
  if tempo_necessario == 'A economia mensal deve ser maior que zero.':
    result_msg = tempo_necessario
  elif tempo_necessario > 1:
    result_msg = f'Você levará aproximadamente {int(tempo_necessario)} meses para atingir a meta financeira de R${meta:.2f}.'
  elif tempo_necessario == 1:
    result_msg = f'Você levará 1 mês para atingir a meta financeira de R${meta:.2f}.'
  else:
    result_msg = 'Você já atingiu a sua meta financeira e pode investir em seus objetivos.'
  return render_template('result.html', result=result_msg)


def calcular_tempo_para_meta(meta, economia_mensal):
  if economia_mensal <= 0:
    return 'A economia mensal deve ser maior que zero.'
  meses_necessarios = meta / economia_mensal
  return meses_necessarios

app.run(host='0.0.0.0')

