package com.example.logistica.entity;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "conductor")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Conductor {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long idConductor;

    private Long idAgente;
    private Long idVehiculo;
    private String nombre;
    private String dni;
    private String telefono;
    private Boolean disponible = true;
}
