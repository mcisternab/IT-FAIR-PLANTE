
function pintar_portada()
{




ctx.fillStyle='#000440';
ctx.fillRect(0,0,juego.width,juego.height);

	
	
	
	contador = 0;
	while (contador < cantidad_espejismos)
	{
	contador = contador + 1;
	if (espejismo[contador].vida>0) { espejismo[contador].dibuja(ctx);}
	}

	ctx.font="16px Arial";
	ctx.fillStyle='#eee';
   	ctx.fillText('avance del pueblo: '+pantalla_juego,40,247)		

}
