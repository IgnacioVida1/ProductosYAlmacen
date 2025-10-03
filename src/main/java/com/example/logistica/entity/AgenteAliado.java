package com.example.logistica.entity;

import jakarta.persistence.*;
import lombok.*;
import java.util.List;

@Entity
@Table(name = "agente_aliado")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class AgenteAliado {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long idAgente;

    private Long idAlmacen;

    @ElementCollection
    @CollectionTable(name = "agente_conductores", joinColumns = @JoinColumn(name = "agente_id"))
    @Column(name = "id_conductor")
    private List<Long> idsConductor;

    private String nombre;
    private String ruc;
    private String telefono;
}
