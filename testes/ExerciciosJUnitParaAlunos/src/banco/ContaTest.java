package banco;

import org.junit.Test;

import junit.framework.TestCase;

// ATIVIDADE MÃO NA MASSA 2
public class ContaTest extends TestCase{

   @Test
   public void testDebitar() {
      Conta c1 = new Conta("123", 50.0);
      try {
         c1.debitar(49.0);
      } catch (OperacaoIlegalException e) {
         fail("Nao deveria ter lancado excecao");
      }
      assertEquals(c1.getSaldo(), 1.0);
   }

   @Test
   public void testDebitarValorNegativo() {
      Conta c1 = new Conta("123", 50.0);
      try {
         c1.debitar(-49.0);
         fail("Deveria ter lancado excecao");
      } catch (OperacaoIlegalException e) {
         assertEquals(c1.getSaldo(), 50.0);
      }
   }

   @Test
   public void testDebitarValorMaiorQueSaldo() {
      Conta c1 = new Conta("123", 50.0);
      try {
         c1.debitar(70.0);
         fail("Não deve ser possível sacar além do saldo");
      } catch (OperacaoIlegalException e) {
         assertEquals(c1.getSaldo(), 50.0);
      }
   }

   @Test
   public void testCreditar() {
      Conta c1 = new Conta("123", 50.0);
      try {
         c1.creditar(49.0);
      } catch (OperacaoIlegalException e) {
         fail("Nao deveria ter lancado excecao");
      }
      assertEquals(c1.getSaldo(), 99.0);
   }

   @Test
   public void testTransferir() throws OperacaoIlegalException {
      Conta c1 = new Conta("123", 50.0);
      Conta c2 = new Conta("456", 50.0);
      try {
         c1.transferir(c2,49.0);
      } catch (OperacaoIlegalException e) {
         fail("Não deveria ter lancado exceção");
      }
      assertEquals(c1.getSaldo(), 1.0);
      assertEquals(c2.getSaldo(), 99.0);         
   }
}
