using UnityEngine;
using UnityEngine.UI;
using TMPro;
using System.Xml;

public class BoardManager : MonoBehaviour
{

    public TMP_Text timerText;
    public TMP_Text winnerText;
    public Sprite emptySprite;
    public GameObject[] cells;
    public Sprite xSprite, oSprite;
    private string currentPlayer = "X";
    private Sprite currentSprite;
    private PilaMovimientos xMoves = new PilaMovimientos();
    private PilaMovimientos oMoves = new PilaMovimientos();
    private float turnTime = 10f;
    private float currentTime;
    public GameObject restartButton;

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

            CheckWinner();
            SwitchPlayer();
        }
    }

    void CheckWinner()
{
    string[,] board = new string[3, 3];

    // Convertimos los sprites actuales a un tablero lógico
    for (int i = 0; i < 9; i++)
    {
        Sprite sprite = cells[i].GetComponent<Image>().sprite;
        if (sprite == xSprite)
            board[i / 3, i % 3] = "X";
        else if (sprite == oSprite)
            board[i / 3, i % 3] = "O";
        else
            board[i / 3, i % 3] = "";
    }

    if (HasPlayerWon(board, currentPlayer))
    {
        timerRunning = false;
        winnerText.gameObject.SetActive(true);
        winnerText.text = $"¡Jugador {currentPlayer} ha ganado!";
        SetBoardInteractable(false);
        restartButton.SetActive(true);
    }
}

bool HasPlayerWon(string[,] board, string player)
{
    // Filas
    for (int i = 0; i < 3; i++)
        if (board[i, 0] == player && board[i, 1] == player && board[i, 2] == player)
            return true;

    // Columnas
    for (int i = 0; i < 3; i++)
        if (board[0, i] == player && board[1, i] == player && board[2, i] == player)
            return true;

    // Diagonal principal
    if (board[0, 0] == player && board[1, 1] == player && board[2, 2] == player)
        return true;

    // Diagonal secundaria
    if (board[0, 2] == player && board[1, 1] == player && board[2, 0] == player)
        return true;

    return false;
}


    void SwitchPlayer()
    {
        currentPlayer = currentPlayer == "X" ? "O" : "X";
        currentSprite = currentPlayer == "X" ? xSprite  : oSprite;

        currentTime = turnTime;
        timerRunning = true;
    }

    void LoseTurn()
    {
        timerRunning = false;

        PilaMovimientos playerMoves = currentPlayer == "X" ? xMoves : oMoves;

        if (!playerMoves.IsEmpty())
        {
            int lastMove = playerMoves.Pop();
            cells[lastMove].GetComponent<Image>().sprite = emptySprite;
        }

        if (playerMoves.IsEmpty())
        {
            timerRunning = false;
            winnerText.text = $"¡Jugador {currentPlayer} ha perdido!";
            winnerText.gameObject.SetActive(true);
            SetBoardInteractable(false);
            restartButton.SetActive(true);

        }
        else
        {
            SwitchPlayer();
        }
    }

    public void RestartGame()
    {
        foreach (GameObject cell in cells)
        {
            cell.GetComponent<Image>().sprite = emptySprite;
            cell.GetComponent<Button>().interactable = true;
        }
    
        xMoves = new PilaMovimientos();
        oMoves = new PilaMovimientos();
    
        currentPlayer = "X";
        currentSprite = xSprite;
        currentTime = turnTime;
        timerRunning = true;
    
        winnerText.gameObject.SetActive(false);
        restartButton.SetActive(false);
    }


    void SetBoardInteractable(bool interactable)
    {
        foreach (GameObject cell in cells)
        {
            cell.GetComponent<Button>().interactable = interactable;
        }
    }



}


