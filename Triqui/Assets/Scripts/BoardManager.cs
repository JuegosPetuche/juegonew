using UnityEngine;
using UnityEngine.UI;


public class BoardManager : MonoBehaviour
{
    public GameObject[] cells; // Debes arrastrar aquí las 9 celdas desde el Inspector
    public Sprite xSprite, oSprite;
    private string currentPlayer = "X";
    private Sprite currentSprite;

    void Start()
    {
        currentSprite = xSprite;
        Debug.Log("xSprite asignado: " + (xSprite != null));

    }

    public void CellClicked(int index)
    {
        Image cellImage = cells[index].GetComponent<Image>();
        if (cellImage.sprite == null || cellImage.sprite.name == "Vacio_0")
        {
            cellImage.sprite = currentSprite;
            SwitchPlayer();
        }
    }

    void SwitchPlayer()
    {
        if (currentPlayer == "X")
        {
            currentPlayer = "O";
            currentSprite = oSprite;
        }
        else
        {
            currentPlayer = "X";
            currentSprite = xSprite;
        }
    }

}