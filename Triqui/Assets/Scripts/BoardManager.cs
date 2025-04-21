using UnityEngine;
using UnityEngine.UI;

public class BoardManager : MonoBehaviour
{
    public GameObject[] cells;
    public Sprite xSprite, oSprite;

    private string currentPlayer = "X";
    private Sprite currentSprite;

    private PilaMovimientos xMoves = new PilaMovimientos();
    private PilaMovimientos oMoves = new PilaMovimientos();

    private float turnTime = 10f;
    private float currentTime;
    private bool timerRunning = false;

    void Start()
    {
        currentSprite = xSprite;
        currentTime = turnTime;
        timerRunning = true;
    }

    void Update()
    {
        if (timerRunning)
        {
            currentTime -= Time.deltaTime;

            if (currentTime <= 0)
            {
                LoseTurn();
            }
        }
    }

    public void CellClicked(int index)
    {
        Image cellImage = cells[index].GetComponent<Image>();

        if (cellImage.sprite.name == "Vacio_0" && timerRunning)
        {
            cellImage.sprite = currentSprite;

            if (currentPlayer == "X")
                xMoves.Push(index);
            else
                oMoves.Push(index);

            SwitchPlayer();
        }
    }

    void SwitchPlayer()
    {
        currentPlayer = currentPlayer == "X" ? "O" : "X";
        currentSprite = currentPlayer == "X" ? xSprite : oSprite;

        currentTime = turnTime;
        timerRunning = true;
    }

    void LoseTurn()
    {
        timerRunning = false;

        Debug.Log(currentPlayer + " perdió su turno por inactividad.");

        PilaMovimientos playerMoves = currentPlayer == "X" ? xMoves : oMoves;

        if (!playerMoves.IsEmpty())
        {
            int lastMove = playerMoves.Pop();
            cells[lastMove].GetComponent<Image>().sprite.name = "Vacio_0";
        }

        if (playerMoves.IsEmpty())
        {
            Debug.Log(currentPlayer + " ha perdido todos sus movimientos. ¡Pierde la partida!");
            // Aquí puedes agregar lógica para mostrar derrota, reiniciar, etc.
        }
        else
        {
            SwitchPlayer();
        }
    }
}
