public class PilaMovimientos
{
    private NodoMovimiento top;
    private int count;

    public void Push(int index)
    {
        NodoMovimiento nuevo = new NodoMovimiento(index);
        nuevo.siguiente = top;
        top = nuevo;
        count++;
    }

    public int Pop()
    {
        if (IsEmpty())
            throw new System.InvalidOperationException("La pila está vacía");

        int index = top.index;
        top = top.siguiente;
        count--;
        return index;
    }

    public bool IsEmpty()
    {
        return top == null;
    }

    public int Count()
    {
        return count;
    }

}

