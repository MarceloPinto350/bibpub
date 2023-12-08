package fila;

import org.junit.Test;

import junit.framework.TestCase;

// ATIVIDADE MÃO NA MASSA 3
public class FilaTest extends TestCase{

   @Test
   public void testInsereNaFila() {
      Fila f1 = new Fila();
      try {
         f1.insereNaFila(49.0);
         f1.insereNaFila(38.0);
         f1.insereNaFila(27.0);
         f1.insereNaFila(16.0);
         f1.insereNaFila(5.0);         

      } catch (FilaCheiaException e) {
         fail("Não deveria ter lancado exceção");
      }
      assertEquals(f1.getFim(), 4);
   }

   @Test
   public void testRemoveDaFila() {
      Fila f1 = new Fila();
      try {
         f1.insereNaFila(49.0);
         f1.insereNaFila(38.0);
         f1.insereNaFila(27.0);
         f1.insereNaFila(16.0);
         f1.insereNaFila(5.0);    
         //assertEquals(f1.getFim(), 4);     //Esse teste está correto
         try {
            f1.removeDaFila();
            assertEquals(f1.getFim(), 3);   //Esse teste está incorreto pois há erro na remoção da fila
         } catch (FilaVaziaException e) {
            fail("Não deveria ter lancado exceção e fila vazia");
         }
      } catch (FilaCheiaException e) {
         fail("Não deveria ter lancado exceção de fila cheia");
      }
   }


}
